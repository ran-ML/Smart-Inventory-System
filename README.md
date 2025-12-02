# Smart-Inventory-System
Machine learning system for demand forecasting, anomaly detection, and automated stock recommendations for retail inventory optimization

# Retail Forecasting + Anomaly Detection (XGBoost)


Project ini menyediakan pipeline end-to-end untuk memprediksi penjualan dan mendeteksi anomali menggunakan XGBoost (forecast) dan IsolationForest (anomaly).


## Cara pakai
1. Install requirements
2. Tempatkan dataset di `data/` dengan kolom `tanggal` dan `terjual` (sesuaikan `target_col` jika beda)
3. Jalankan `src/retail_pipeline.py` dari notebook:


from src.retail_pipeline import RetailPipeline
pipe = RetailPipeline(target_col='terjual')
pipe.run('data/dataset_retail.csv')


4. Load model dan lakukan prediksi pada data baru


## Struktur
(Lihat dokumentasi di repository)
