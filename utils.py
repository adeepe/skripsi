import torch
import matplotlib.pyplot as plt
import pandas as pd

def data4pred(model, dataset, dataloader, device):    
    preds, targets = [], []
    hidden = None
    with torch.no_grad():
        model.eval()
        for inputs, target in dataloader:
            inputs = inputs.to(device)
            
            output, hidden = model(inputs, hidden)
            preds += output.flatten().tolist()
            targets += target.flatten().tolist()
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.plot(dataset.target_ticks, targets, 'k-', label="data")  # Garis lurus hitam
    plt.plot(dataset.target_ticks, preds, 'k--', label="pred")  # Garis putus-putus hitam
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.legend()
    return preds, targets
    
def pred4pred(model, dataset, dataloader, device, n_prior=3, n_forecast=19):
    preds, targets = [], []
    hidden = None    
    end = n_prior + n_forecast    
    with torch.no_grad():
        model.eval()       
        for idx, (inputs, target) in enumerate(dataloader):
            if idx == end:
                break
            elif idx > n_prior:
                inputs[0, 0, 0] = preds[-1]
                
            inputs = inputs.to(device)
            output, hidden = model(inputs, hidden)
            
            if idx > n_prior:
                preds.append(output.flatten().tolist()[-1])
            else:
                preds += output.flatten().tolist()   
            targets += target.flatten().tolist()

  
    # Mengatur font family menjadi Times New Roman
    plt.rcParams['font.family'] = 'Times New Roman'

    # Plotting dengan garis lurus dan putus-putus hitam putih
    plt.plot(dataset.target_ticks[:n_prior], targets[:n_prior], 'k-', label="history_data")  # Garis lurus hitam
    plt.plot(dataset.target_ticks[n_prior:end], targets[n_prior:], 'k-', label="unseen_data", alpha=0.3)  # Garis putus-putus hitam
    plt.plot(dataset.target_ticks[:end], preds, 'k--', label="prediction")  # Garis lurus hitam untuk prediksi
    plt.axvline(dataset.target_ticks[n_prior], color='k', linestyle="--", linewidth=1)  # Garis putus-putus hitam vertikal
    plt.legend()

    plt.xlabel('X Label', fontsize=12)
    plt.ylabel('Y Label', fontsize=12)
    return preds, targets

def predict_long_term(model, dataset, dataloader, device, n_prior=21, n_forecast=1, months_ahead=60):
    preds, targets = [], []
    hidden = None    
    end = n_prior + n_forecast    
    with torch.no_grad():
        model.eval()
        for idx, (inputs, target) in enumerate(dataloader):
            if idx == end:
                break
            elif idx > n_prior:
                inputs[0, 0, 0] = preds[-1]
                
            inputs = inputs.to(device)
            output, hidden = model(inputs, hidden)
            
            if idx > n_prior:
                preds.append(output.flatten().tolist()[-1])
            else:
                preds += output.flatten().tolist()   
            targets += target.flatten().tolist()

        # Extend predictions for the specified number of months ahead
        for _ in range(months_ahead):
            inputs[0, 0, 0] = preds[-1]
            inputs = inputs.to(device)
            output, hidden = model(inputs, hidden)
            preds.append(output.flatten().tolist()[-1])

    # Update target_ticks for extended predictions
    extended_ticks = list(dataset.target_ticks[:end]) + [dataset.target_ticks[-1] + pd.DateOffset(months=i) for i in range(1, months_ahead + 1)]
  
    # Mengatur font family menjadi Times New Roman
    plt.rcParams['font.family'] = 'Times New Roman'

    # Plotting dengan garis lurus dan putus-putus hitam putih
    plt.plot(dataset.target_ticks[:n_prior], targets[:n_prior], 'k-', label="history_data")  # Garis lurus hitam
    plt.plot(dataset.target_ticks[n_prior:end], targets[n_prior:], 'k-', label="unseen_data", alpha=0.3)  # Garis putus-putus hitam
    plt.plot(extended_ticks, preds, 'k--', label="prediction")  # Garis lurus hitam untuk prediksi
    plt.axvline(dataset.target_ticks[n_prior], color='k', linestyle="--", linewidth=1)  # Garis putus-putus hitam vertikal
    plt.legend()

    plt.xlabel('X Label', fontsize=12)
    plt.ylabel('Y Label', fontsize=12)
    return preds, targets