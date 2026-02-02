import streamlit as st
import pandas as pd

# Konfigurasi Halaman HP agar pas
st.set_page_config(page_title="Data Generus", layout="centered")

st.title("📱 Evaluasi Generus")

# Input Data
with st.form("form_input", clear_on_submit=True):
    nama = st.text_input("Nama Lengkap")
    kelompok = st.text_input("Kelompok")
    jk = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    kelas = st.text_input("Kelas")
    
    st.subheader("Target Materi")
    alquran = st.text_input("Makna Al-Quran")
    hadist = st.text_input("Makna Al-Hadist")
    doa = st.text_input("Hafalan Doa")
    dalil = st.text_input("Hafalan Dalil")
    progres = st.slider("Persentase Evaluasi (%)", 0, 100, 0)
    
    submitted = st.form_submit_button("Simpan Data")

# Penanganan Data Sederhana (Disimpan dalam sesi ini)
if "db_siswa" not in st.session_state:
    st.session_state.db_siswa = []

if submitted:
    data_baru = {
        "Nama": nama, "Kelompok": kelompok, "JK": jk, "Kelas": kelas,
        "Al-Quran": alquran, "Hadist": hadist, "Doa": doa, "Dalil": dalil, "Progres": f"{progres}%"
    }
    st.session_state.db_siswa.append(data_baru)
    st.success("Data Berhasil Dicatat!")

# Tampilkan Daftar
st.divider()
st.subheader("📋 Daftar Siswa")
if st.session_state.db_siswa:
    df = pd.DataFrame(st.session_state.db_siswa)
    st.dataframe(df)
else:
    st.info("Belum ada data.")
