# Skripsi Project

## Pengantar

Project ini berisi skrip dan model untuk analisis data skripsi. Project ini menggunakan Flask untuk membuat API server dan memiliki halaman web statis untuk visualisasi dengan model yang digunakan adalah LSTM.

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dependensi dan menjalankan aplikasi.

### 1. Clone Repository

Clone repository ini ke direktori lokal Anda.

```sh
git clone https://github.com/adeepe/skripsi.git
cd skripsi


### 2. Buat dan Aktifkan Conda Environment
Buat conda environment dan aktifkan.

```sh
conda env create -f environment.yml
conda activate skripsi-env


### 3. Jalankan Flask API Server
Jalankan Flask API server dengan perintah berikut.

```sh
conda env create -f environment.yml
conda activate skripsi
python app.py


### 4. Akses Halaman Web
Buka browser dan akses halaman web di \static/index.html\.

```sh
open static/index.html

## Struktur Proyek
Berikut adalah struktur project ini:
```sh
skripsi/
├── data/
├── model/
├── static/
│   └── index.html
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

## Perbandingan Model
Untuk melihat perbandingan model, Anda bisa membuka notebook berikut:

- \SKRIPSI_ARIMA.ipynb\
- \SKRIPSI_BiLSTM_SUMMARY.ipynb\
- \SKRIPSI_EXPONENTIAL_SMOOTHING.ipynb\
- \SKRIPSI_OLS.ipynb\

Notebook-notebook tersebut berisi analisis dan perbandingan performa dari berbagai model yang digunakan dalam proyek ini.

## Catatan Tambahan
Pastikan semua dependensi telah diinstal dengan benar sebelum menjalankan aplikasi. Jika Anda mengalami masalah, periksa versi Python dan dependensi yang diinstal.

