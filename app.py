	import streamlit as st
import joblib
import numpy as np

model = joblib.load('model_zonasi.pkl')

st.set_page_config(page_title="PPDB SD Zonasi Predictor", layout="centered")
st.title("🏫 Sistem Seleksi PPDB SD Berbasis Zonasi")
st.write("Aplikasi Machine Learning untuk memprediksi kelayakan penerimaan siswa baru.")
st.markdown("---")

st.subheader("📊 Input Data Calon Siswa")
jarak = st.number_input("Jarak Rumah ke Sekolah (Meter)", min_value=10, max_value=10000, value=500, step=50)
umur = st.number_input("Umur Anak (Tahun)", min_value=5.0, max_value=10.0, value=7.0, step=0.1)
nilai = st.number_input("Nilai Kesiapan Sekolah (50 - 100)", min_value=50, max_value=100, value=80, step=1)

if st.button("Cek Status Penerimaan"):
    data_input = np.array([[jarak, umur, nilai]])
    prediksi = model.predict(data_input)

    st.markdown("---")
    st.subheader("📢 Hasil Keputusan:")
    if prediksi[0] == 1:
        st.success("🎉 **DITERIMA!** Calon siswa memenuhi kriteria zonasi.")
    else:
        st.error("❌ **DITOLAK!** Jarak terlalu jauh atau umur belum mencukupi.")