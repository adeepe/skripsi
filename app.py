import pandas as pd
import logging
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.seasonal import STL

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.rnn = torch.nn.LSTM(input_size=1, hidden_size=8, num_layers=2, batch_first=True)
        self.fc = torch.nn.Linear(in_features=8, out_features=1)

    def forward(self, x, hidden=None):
        out, hidden = self.rnn(x, hidden)
        out = self.fc(out[:, -1, :])  # Take output from last time step
        return out, hidden

def load_data(csv_path):
    df = pd.read_csv(csv_path, delimiter=';')
    df['Date'] = pd.to_datetime(df['THBL'], format='%Y%m')
    df.set_index('Date', inplace=True)
    df.drop(columns=['THBL'], inplace=True)
    return df

class TimeSeriesDataset(Dataset):
    def __init__(self, data, target_column, sequence_length):
        self.data = data
        self.target_column = target_column
        self.sequence_length = sequence_length
        self.data_values = self.data[target_column].values

    def __len__(self):
        return len(self.data) - self.sequence_length

    def __getitem__(self, idx):
        x = self.data_values[idx:idx+self.sequence_length]
        y = self.data_values[idx+self.sequence_length]
        return torch.tensor(x, dtype=torch.float32).unsqueeze(1), torch.tensor(y, dtype=torch.float32)

def predict_long_term(model, data, sequence_length, device, months_ahead=60):
    model.eval()
    predictions = []

    with torch.no_grad():
        input_seq = data[-sequence_length:]  # Initial input sequence from the end of the data
        input_seq = torch.tensor(input_seq, dtype=torch.float32).unsqueeze(0).unsqueeze(2).to(device)

        for _ in range(months_ahead):
            output, _ = model(input_seq)
            predictions.append(output.item())

            # Create new input sequence: remove first element and append the new prediction
            output = output.unsqueeze(0).unsqueeze(2) if output.dim() == 1 else output.view(1, 1, 1)
            input_seq = torch.cat((input_seq[:, 1:, :], output), dim=1)

    return predictions

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        months_ahead = int(data['months_ahead'])
        logging.debug(f"Months ahead: {months_ahead}")
    except ValueError:
        return jsonify({"error": "Invalid input, please enter an integer"}), 400

    csv_path = 'data/JOG_monthly.csv'  # Path to the CSV file
    
    if not os.path.exists(csv_path):
        logging.error("CSV file not found")
        return jsonify({"error": "CSV file not found"}), 404
    
    try:
        data = load_data(csv_path)
        logging.debug("Data loaded successfully")
        
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data["GWH_JUAL"].values.reshape(-1, 1))
        logging.debug("Data scaled successfully")
        
        # Decompose the data to get the seasonal component
        result = STL(data['GWH_JUAL'], seasonal=13).fit()
        seasonal_component = result.seasonal.values
        logging.debug("Seasonal component extracted successfully")
        
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        logging.debug(f"Using device: {device}")
        
        model = MyModel()
        model_path = 'model.pth'
        if not os.path.exists(model_path):
            logging.error("Model file not found")
            return jsonify({"error": "Model file not found"}), 404
        
        model.load_state_dict(torch.load(model_path, map_location=device))
        model.to(device)
        model.eval()
        logging.debug("Model loaded successfully")

        preds_scaled = predict_long_term(model, scaled_data.flatten(), 12, device, months_ahead=months_ahead)
        preds = scaler.inverse_transform(np.array(preds_scaled).reshape(-1, 1)).flatten()
        logging.debug("Predictions made successfully")
        
        # Add seasonal component to the predictions
        seasonal_component_forecast = np.tile(seasonal_component[-12:], months_ahead // 12 + 1)[:months_ahead]
        preds_seasonal = preds + seasonal_component_forecast
        
        return jsonify({"predictions": preds_seasonal.tolist()})
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
