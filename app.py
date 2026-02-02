import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Generus Desa 1", layout="wide")

# --- DATABASE TARGET LENGKAP (Tahun 1 & 2, Semua Kelas) ---
TARGET_MASTER = {
    "Kelas A": {
        "Tahun Pertama": {
            "Juli": {"quran": "Al Angkabut 45-Arrum 24", "hadist": "Kitabussholah 1-18", "surat": "An-Nas s/d Al-Kafirun", "doa": "Doa kumpulan nabi muhammad", "dalil": "Mengaji (2)"},
            "Agustus": {"quran": "Arrum 25-Luqman 11", "hadist": "Kitabussholah 19-36", "surat": "Al-Kausar s/d Al-Fil", "doa": "Doa berlindung amal jelek", "dalil": "Mengamal (2)"},
            "September": {"quran": "Luqman 12-Assajadah 20", "hadist": "Kitabussholah 37-54", "surat": "Al-Humazah s/d Al-Adiyat", "doa": "Penderesan", "dalil": "Deres sebelumnya"},
            "Oktober": {"quran": "Assajadah 21-Al Ahzab 30", "hadist": "Kitabussholah 55-72", "surat": "Al-Qori'ah s/d Az-Zalzalah", "doa": "Doa lindung dari 4 hal", "dalil": "Membela (2)"},
            "November": {"quran": "Al Ahzab 31-62", "hadist": "Kitabussholah 73-90", "surat": "Al-Bayyinah s/d Al-Qodr", "doa": "Doa lindung dari syirik", "dalil": "Jamaah (2)"},
            "Desember": {"quran": "Al Ahzab 63-Saba' 31", "hadist": "Kitabussholah 91-108", "surat": "Al-Alaq s/d At-Tin", "doa": "Penderesan", "dalil": "Deres sebelumnya"},
        },
        "Tahun Kedua": {
            "Juli": {"quran": "Azzumar 32-74", "hadist": "Adab 66-83", "surat": "Al-Insyirah s/d Ad-Duha", "doa": "Doa lindung jelek anggota badan", "dalil": "Deres (4)"},
            "Agustus": {"quran": "Azzumar 75-Gofir 40", "hadist": "Adab 84-100", "surat": "Al-Lail s/d Asy-Syams", "doa": "Doa masuk pasar", "dalil": "Deres (4)"},
        }
    },
    "Kelas B": {
        "Tahun Pertama": {
            "Juli": {"quran": "Addariyat 31-Al Qomar 6", "hadist": "Adillah 1-20", "surat": "At-Toriq", "doa": "Doa tempat baru", "dalil": "Berdoa (2)"},
        }
    },
    "Kelas C": {
        "Tahun Pertama": {
            "Juli": {"quran": "Yusuf 53-111", "hadist": "Ahkam 1-22", "surat": "Al-Buruj", "doa": "Doa pr bp imam 1-7", "dalil": "Amanah (2)"},
        }
    }
}

st.title("📊 Sistem Evaluasi Full Kurikulum Generus")

# --- IDENTITAS & TARGET ---
with st.sidebar:
    st.header("👤 Data Input")
    nama = st.text_input("Nama Lengkap")
    kls = st.selectbox("Pilih Kelas", ["Kelas A", "Kelas B", "Kelas C"])
    thn = st.radio("Pilih Tahun", ["Tahun Pertama", "Tahun Kedua"])
    bln = st.selectbox("Pilih Bulan", ["Juli", "Agustus", "September", "Oktober", "November", "Desember", "Januari", "Februari", "Maret", "April", "Mei", "Juni"])

# Menampilkan Target Otomatis
target = TARGET_MASTER.get(kls, {}).get(thn, {}).get(bln, {"quran": "-", "hadist": "-", "surat": "-", "doa": "-", "dalil": "-"})

st.info(f"🎯 **Target {bln} ({thn}) untuk {kls}:**")
t_col1, t_col2 = st.columns(2)
with t_col1:
    st.write(f"📖 **Quran:** {target['quran']}")
    st.write(f"📜 **Hadist:** {target['hadist']}")
    st.write(f"🕋 **Surat:** {target['surat']}")
with t_col2:
    st.write(f"🙏 **Doa:** {target['doa']}")
    st.write(f"💡 **Dalil:** {target['dalil']}")

st.divider()

# --- PENILAIAN ---
st.subheader("📉 Detail Penilaian Persentase (%)")

def input_materi_detail(label, key_p):
    with st.expander(f"Penilaian {label}", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1: m = st.number_input(f"Materi (%)", 0, 100, 0, key=f"{key_p}m")
        with c2: n = st.number_input(f"Makna (%)", 0, 100, 0, key=f"{key_p}n")
        with c3: k = st.number_input(f"Ket (%)", 0, 100, 0, key=f"{key_p}k")
    return (m + n + k) / 3

# Baris 1: Quran & Hadist (3 Kategori)
col_q, col_h = st.columns(2)
with col_q: total_q = input_materi_detail("Al-Quran", "q")
with col_h: total_h = input_materi_detail("Al-Hadist", "h")

# Baris 2: Surat, Doa, Dalil (1 Kategori)
st.markdown("#### Penilaian Hafalan")
col_s, col_d, col_l = st.columns(3)
with col_s: total_s = st.number_input("Hafalan Surat (%)", 0, 100, 0)
with col_d: total_d = st.number_input("Hafalan Doa (%)", 0, 100, 0)
with col_l: total_l = st.number_input("Hafalan Dalil (%)", 0, 100, 0)

# Simpan
if st.button("💾 SIMPAN DATA EVALUASI", use_container_width=True):
    if nama:
        if "rekap" not in st.session_state: st.session_state.rekap = []
        avg = (total_q + total_h + total_s + total_d + total_l) / 5
        st.session_state.rekap.append({
            "Nama": nama, "Kelas": kls, "Tahun": thn, "Bulan": bln,
            "Quran": f"{total_q:.1f}%", "Hadist": f"{total_h:.1f}%",
            "Surat": f"{total_s}%", "Doa": f"{total_d}%", "Dalil": f"{total_l}%",
            "Rata-rata": f"{avg:.1f}%"
        })
        st.success(f"Data {nama} berhasil disimpan!")

# --- REKAP TABEL ---
st.divider()
if "rekap" in st.session_state:
    st.subheader("📋 Rekapitulasi Nilai")
    st.dataframe(pd.DataFrame(st.session_state.rekap), use_container_width=True)
