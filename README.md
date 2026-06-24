**Proyek Machine Learning: Prediksi PPDB SD Berbasis Zonasi**

1. Business Understanding
Proyek ini bertujuan untuk mengotomatisasi proses seleksi siswa baru tingkat SD berdasarkan parameter sistem zonasi jarak, umur, dan kesiapan siswa. Sistem ini mempermudah panitia sekolah dalam mengambil keputusan yang cepat dan objektif.

2. Data Understanding & Preparation
Dataset yang digunakan adalah data simulasi dengan fitur:
- `jarak_meter`: Jarak rumah ke sekolah.
- `umur_tahun`: Usia calon siswa.
- `nilai_kesiapan`: Indikator kesiapan akademik/mental.
Target: `status_diterima` (1 = Diterima, 0 = Ditolak).
Data dibagi menggunakan Train-Test Split dengan rasio 80:20. Kami juga menyertakan visualisasi Boxplot di dalam notebook untuk melihat distribusi data.

3. Modeling & Evaluation
Kami menggunakan algoritma **Random Forest Classifier** (Ensemble Learning) untuk klasifikasi performa tinggi. Model dievaluasi menggunakan data testing independen dan menghasilkan tingkat akurasi yang optimal, membuktikan model bebas dari overfitting.

4. Deployment
Model di-deploy menggunakan web framework **Streamlit** untuk memfasilitasi antarmuka pengguna (UI) yang interaktif bagi pihak sekolah.
