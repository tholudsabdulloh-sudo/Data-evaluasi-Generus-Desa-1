import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Generus Desa 1", layout="wide")

# --- DATA TARGET (Sesuai Kurikulum Foto) ---
TARGET_MASTER = {
    "Kelas A": {
        "Tahun Pertama": {
            "Juli": {"quran": "Al Angkabut 45", "hadist": "Kitabussholah 1", "doa": "Doa nabi muhammad", "dalil": "Mengaji (2)"},
            "Agustus": {"quran": "Arrum 25", "hadist": "Kitabussholah 19", "doa": "Doa amal jelek", "dalil": "Mengamal (2)"}
        "Tahun Kedua": {
            "Juli": {"quran": "Azzumar 32", "hadist": "Adab 66", "doa": "Doa lindung jelek anggota badan", "dalil": "Mengaji (lanjutan)"},
        }
    }
    # Tambahkan data lainnya sesuai pola di atas
}

st.title("📊 Sistem Evaluasi Detail Generus")

# --- BAGIAN 1: IDENTITAS & TARGET ---
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        nama = st.text_input("Nama Lengkap")
        kls = st.selectbox("Pilih Kelas", ["Kelas A", "Kelas B", "Kelas C"])
        thn = st.radio("Pilih Tahun", ["Tahun Pertama", "Tahun Kedua"], horizontal=True)
        bln = st.selectbox("Bulan", ["Juli", "Agustus", "September", "Oktober", "November", "Desember", "Januari", "Februari", "Maret", "April", "Mei", "Juni"])
    
    with c2:
        target = TARGET_MASTER.get(kls, {}).get(thn, {}).get(bln, {"quran": "-", "hadist": "-", "doa": "-", "dalil": "-"})
        st.info(f"🎯 **Target {bln} ({thn}):**")
        st.write(f"📖 **Quran:** {target['quran']} | 📜 **Hadist:** {target['hadist']}")
        st.write(f"🙏 **Doa:** {target['doa']} | 💡 **Dalil:** {target['dalil']}")

st.divider()

# --- BAGIAN 2: PENILAIAN DETAIL ---
st.subheader("KategoriEvaluasi")

# Fungsi untuk menghitung rata-rata sub-kategori
def calc_sub(materi, makna, ket):
    return (materi + makna + ket) / 3

col_q, col_h = st.columns(2)

with col_q:
    st.markdown("#### 📖 Makna Al-Quran")
    q_mat = st.number_input("Materi Quran (%)", 0, 100, 0, key="q1")
    q_mak = st.number_input("Makna Quran (%)", 0, 100, 0, key="q2")
    q_ket = st.number_input("Keterangan Quran (%)", 0, 100, 0, key="q3")
    total_q = calc_sub(q_mat, q_mak, q_ket)
    st.write(f"**Hasil Akhir Quran: {total_q:.1f}%**")

with col_h:
    st.markdown("#### 📜 Makna Al-Hadist")
    h_mat = st.number_input("Materi Hadist (%)", 0, 100, 0, key="h1")
    h_mak = st.number_input("Makna Hadist (%)", 0, 100, 0, key="h2")
    h_ket = st.number_input("Keterangan Hadist (%)", 0, 100, 0, key="h3")
    total_h = calc_sub(h_mat, h_mak, h_ket)
    st.write(f"**Hasil Akhir Hadist: {total_h:.1f}%**")

st.markdown("---")
col_d, col_l = st.columns(2)

with col_d:
    st.markdown("#### 🙏 Hafalan Doa")
    total_d = st.number_input("Nilai Hafalan Doa (%)", 0, 100, 0)

with col_l:
    st.markdown("#### 💡 Hafalan Dalil")
    total_l = st.number_input("Nilai Hafalan Dalil (%)", 0, 100, 0)
with col_l:
    st.markdown("#### 💡 Hafalan Surat")
    total_l = st.number_input("Nilai Hafalan Dalil (%)", 0, 100, 0)


# Skor Akhir Keseluruhan
skor_akhir = (total_q + total_h + total_d + total_l) / 4

if st.button("💾 SIMPAN DATA EVALUASI"):
    if nama:
        if "db_permanen" not in st.session_state: st.session_state.db_permanen = []
        st.session_state.db_permanen.append({
            "Nama": nama, "Kelas": kls, "Bulan": bln,
            "Quran": f"{total_q:.1f}%", "Hadist": f"{total_h:.1f}%",
            "Doa": f"{total_d}%", "Dalil": f"{total_l}%",
            "Total": f"{skor_akhir:.1f}%"
        })
        st.success(f"Evaluasi {nama} berhasil dicatat!")
    else:
        st.error("Nama harus diisi!")

# --- BAGIAN 3: TABEL REKAP ---
st.divider()
if "db_permanen" in st.session_state and st.session_state.db_permanen:
    st.write("### 📋 Rekap Hasil")
    st.dataframe(pd.DataFrame(st.session_state.db_permanen), use_container_width=True)
