# Skripsi Implementasi Prediksi Penggunaan Energi Listrik Menggunakan Metode Long Short-Term Memory

## Pengantar

Penelitian ini bertujuan untuk menganalisis dan memprediksi penggunaan energi listrik di Provinsi D.I. Yogyakarta hingga tahun 2030 berdasarkan data penjualan bulanan dari tahun 2015 hingga 2024 yang diperoleh dari PLN UP3 Yogyakarta. Data menunjukkan tren peningkatan konsumsi energi listrik dengan fluktuasi musiman. 
Model Long Short-Term Memory (LSTM) digunakan untuk prediksi, dengan hasil pelatihan menunjukkan nilai Mean Squared Error (MSE) terendah sebesar 0.0158 pada data training. Evaluasi data testing menghasilkan Mean Absolute Error (MAE) sebesar 0.0762, MSE sebesar 0.0104, dan koefisien determinasi (R²) sebesar 0.5138, menunjukkan bahwa model mampu mengenali sekitar 51.38% variansi dalam variabel dependen.
Model LSTM menunjukkan performa lebih baik dibandingkan dengan BiLSTM, Exponential Smoothing (ES), ARIMA, dan Ordinary Least Squares (OLS). Implementasi model dilakukan melalui API Flask yang diuji dengan Postman, dan hasil prediksi diintegrasikan ke dalam website sederhana, memungkinkan pengguna untuk melihat hasil prediksi penggunaan energi listrik. Penelitian ini menyimpulkan bahwa model LSTM lebih efektif dibandingkan metode lain yang digunakan dalam penelitian ini terkait prediksi penggunaan energi listrik di D.I. Yogyakarta.

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dependensi dan menjalankan aplikasi.

### 1. Clone Repository

Clone repository ini ke direktori lokal Anda.

```sh
git clone https://github.com/adeepe/skripsi.git
cd skripsi
```

### 2. Buat dan Aktifkan Conda Environment
Buat conda environment dan aktifkan.

```sh
conda env create -f environment.yml
conda activate skripsi-env
```

### 3. Jalankan Flask API Server
Jalankan Flask API server dengan perintah berikut.

```sh
conda env create -f environment.yml
conda activate skripsi
python app.py
```

### 4. Akses Halaman Web
Buka browser dan akses halaman web di \static/index.html\.

```sh
open static/index.html
```
## Struktur Proyek
Berikut adalah struktur project ini:
```sh
skripsi/
├── data/
│   └── JOG_MONTHLY.csv
├── model/
├── static/
│   └── index.html
│   └── style.css
│   └── scripts.js
├── README.md
├── SKRIPSI_ANALISIS_DATA.ipynb
├── SKRIPSI_ARIMA.ipynb
├── SKRIPSI_BiLSTM_SUMMARY.ipynb
├── SKRIPSI_DEPLOY.ipynb
├── SKRIPSI_EXPONENTIAL_SMOOTHING.ipynb
├── SKRIPSI_LSTM_SUMMARY.ipynb
├── SKRIPSI_LSTM.ipynb
├── SKRIPSI_MULTIVARIATE_LSTM.ipynb
├── SKRIPSI_OLS.ipynb
├── app.py
├── environment.yml
└── model.pth
```
## Perbandingan Model
Untuk melihat perbandingan model, Anda bisa membuka notebook berikut:

- [SKRIPSI_ARIMA.ipynb](https://github.com/adeepe/skripsi/blob/master/SKRIPSI_ARIMA.ipynb)
- [SKRIPSI_BiLSTM.ipynb](https://github.com/adeepe/skripsi/blob/master/SKRIPSI_BiLSTM.ipynb)
- [SKRIPSI_EXPONENTIAL_SMOOTHING.ipynb](https://github.com/adeepe/skripsi/blob/master/SKRIPSI_EXPONENTIAL_SMOOTHING.ipynb)
- [SKRIPSI_OLS.ipynb](https://github.com/adeepe/skripsi/blob/master/SKRIPSI_OLS.ipynb)
- [SKRIPSI_LSTM.ipynb](https://github.com/adeepe/skripsi/blob/master/SKRIPSI_LSTM.ipynb)

Notebook-notebook tersebut berisi analisis dan perbandingan performa dari berbagai model yang digunakan dalam proyek ini.

## Catatan Tambahan
Pastikan semua dependensi telah diinstal dengan benar sebelum menjalankan aplikasi. Jika Anda mengalami masalah, periksa versi Python dan dependensi yang diinstal.

