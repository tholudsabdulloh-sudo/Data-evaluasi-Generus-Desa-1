import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Generus Desa 1", layout="wide")

# --- DATABASE TARGET LENGKAP (Tahun 1 & 2, Semua Kelas) ---
TARGET_MASTER = {
    "Kelas A": {
        "Tahun Pertama": {
            "Juli": {"quran": "Al Angkabut 45 - Arrum 24", "hadist": "Kitabussholah 1-18", "doa": "Doa kumpulan nabi muhammad", "dalil": "Mengaji (2 dalil)"},
            "Agustus": {"quran": "Arrum 25 - Luqman 11", "hadist": "Kitabussholah 19-36", "doa": "Doa berlindung amal jelek", "dalil": "Mengamal (2 dalil)"},
            "September": {"quran": "Luqman 12 - Assajadah 20", "hadist": "Kitabussholah 37-54", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Oktober": {"quran": "Assajadah 21 - Al Ahzab 30", "hadist": "Kitabussholah 55-72", "doa": "Doa lindung dari 4 hal", "dalil": "Membela (2 dalil)"},
            "November": {"quran": "Al Ahzab 31 - 62", "hadist": "Kitabussholah 73-90", "doa": "Doa lindung dari syirik", "dalil": "Jamaah (2 dalil)"},
            "Desember": {"quran": "Al Ahzab 63 - Saba' 31", "hadist": "Kitabussholah 91-108", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Januari": {"quran": "Saba' 32 - Fatir 19", "hadist": "Kitabussholah 109-126", "doa": "Doa solat mayit", "dalil": "Toat (2 dalil)"},
            "Februari": {"quran": "Fatir 20 - Yasin 27", "hadist": "Kitabussholah 127-144", "doa": "Doa Krukunan", "dalil": "Bersyukur (2 dalil)"},
            "Maret": {"quran": "Yasin 28 - Assofat 24", "hadist": "Kitabussholah 145 - Adab 11", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "April": {"quran": "Assofat 25 - 153", "hadist": "Adab 12-29", "doa": "Doa pengampunan", "dalil": "Mengagungkan (2 dalil)"},
            "Mei": {"quran": "Assofat 154 - Sot 61", "hadist": "Adab 30-47", "doa": "Doa perlindungan", "dalil": "Mempersungguh (2 dalil)"},
            "Juni": {"quran": "Sot 62 - Azzumar 31", "hadist": "Adab 48-65", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
        },
        "Tahun Kedua": {
            "Juli": {"quran": "Azzumar 32-74", "hadist": "Adab 66-83", "doa": "Doa lindung jelek anggota badan", "dalil": "Deres dalil (4 dalil)"},
            "Agustus": {"quran": "Azzumar 75 - Gofir 40", "hadist": "Adab 84-100", "doa": "Doa masuk pasar", "dalil": "Deres dalil (4 dalil)"},
            "September": {"quran": "Gofir 41-85", "hadist": "Nawafil 1-19", "doa": "Penderesan", "dalil": "Deres dalil (4 dalil)"},
            "Oktober": {"quran": "Fussilat 1-46", "hadist": "Nawafil 20-38", "doa": "Doa menjenguk orang sakit", "dalil": "Deres dalil (4 dalil)"},
            "November": {"quran": "Fussilat 47 - Assuro' 31", "hadist": "Nawafil 39-56", "doa": "Doa mensyukuri nikmat", "dalil": "Deres dalil (4 dalil)"},
            "Desember": {"quran": "Assuro' 32 - Aszuhruf 33", "hadist": "Nawafil 57-74", "doa": "Penderesan", "dalil": "Deres dalil (4 dalil)"},
            "Januari": {"quran": "Aszuhruf 34 - Addukhon 18", "hadist": "Nawafil 75-92", "doa": "Doa solat istikhoroh", "dalil": "Deres dalil (4 dalil)"},
            "Februari": {"quran": "Addukhon 19 - Al Jasiyah 32", "hadist": "Nawafil 93 - Da'wat 10", "doa": "Doa mencari ilmu 42", "dalil": "Deres dalil (4 dalil)"},
            "Maret": {"quran": "Al Jasiyah 33 - Al Ahkhof 35", "hadist": "Da'wat 11-28", "doa": "Penderesan", "dalil": "Deres dalil (4 dalil)"},
            "April": {"quran": "Muhammad 1 - Al Fatah 9", "hadist": "Da'wat 29-47", "doa": "Doa pengayoman", "dalil": "Deres dalil (4 dalil)"},
            "Mei": {"quran": "Al Fatah 10 - Al Khujurot 11", "hadist": "Da'wat 48-65", "doa": "Minta surga firdaus", "dalil": "Deres dalil (4 dalil)"},
            "Juni": {"quran": "Al Khujurot 12 - Addariyat 30", "hadist": "Da'wat 66-70", "doa": "Penderesan", "dalil": "Deres dalil (4 dalil)"},
        }
    },
    "Kelas B": {
        "Tahun Pertama": {
            "Juli": {"quran": "Addariyat 31 - Al Qomar 6", "hadist": "Adillah 1-20", "doa": "Doa bertempat di tempat baru", "dalil": "Berdoa (2 dalil)"},
            "Agustus": {"quran": "Al Qomar 7 - Al Waqiah 50", "hadist": "Adillah 21-40", "doa": "Doa mensyukuri nikmat", "dalil": "Alim Faqih (2 dalil)"},
            "September": {"quran": "Al Waqiah 51 - Al Mujadalah 6", "hadist": "Adillah 41-60", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Oktober": {"quran": "Al Mujadalah 7 - Al Mumtahanah 5", "hadist": "Adillah 61-80", "doa": "Doa minta kesabaran", "dalil": "Akhlakul karimah (2 dalil)"},
            "November": {"quran": "Al Mumtahanah 6 - Attagobun 9", "hadist": "Adillah 81-100", "doa": "Doa minta mati syahid", "dalil": "Mandiri (2 dalil)"},
            "Desember": {"quran": "Attagobun 10 - Al Mulk 26", "hadist": "Janawannar 1-20", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Januari": {"quran": "Al Mulk 27 - Nuh 10", "hadist": "Janawannar 21-40", "doa": "Doa mimpi baik & buruk", "dalil": "Rukun (2 dalil)"},
            "Februari": {"quran": "Nuh 11 - Al Qiyamah 19", "hadist": "Janawannar 41-60", "doa": "Doa angin kencang", "dalil": "Kompak (2 dalil)"},
            "Maret": {"quran": "Al Qiyamah 20 - Annaziat 46", "hadist": "Janawannar 61-80", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "April": {"quran": "Abbasa 1 - Al A'la 15", "hadist": "Janawannar 81 - Jannaiz 10", "doa": "Doa pengampunan", "dalil": "Kerja sama baik (2 dalil)"},
            "Mei": {"quran": "Al A'la 16 - Al Bayyinah 7", "hadist": "Jannaiz 11-30", "doa": "Doa perlindungan", "dalil": "Jujur (2 dalil)"},
            "Juni": {"quran": "Al Bayyinah 8 - Annas 6", "hadist": "Jannaiz 31-50", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
        },
        "Tahun Kedua": {
            "Juli": {"quran": "Al A'rof 88-149", "hadist": "Jannaiz 51-70", "doa": "Doa sholat tasbih", "dalil": "Berdoa (lanjutan)"},
            "Agustus": {"quran": "Al A'rof 150-195", "hadist": "K Soum 1-10", "doa": "Doa minum air zam-zam", "dalil": "Alim Faqih (lanjutan)"},
            "September": {"quran": "Al A'rof 196 - Al Anfal 45", "hadist": "K Soum 11-30", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Oktober": {"quran": "Al Anfal 46 - Attaubat 20", "hadist": "K Soum 31-50", "doa": "Doa minta naik haji", "dalil": "Akhlakul karimah (lanjutan)"},
        }
    },
        "Kelas C": {
        "Tahun Pertama": {
            "Juli": {"quran": "Yusuf 53-111", "hadist": "Ahkam 1-22", "surat": "Al-Buruj", "doa": "Doa pr bp imam 1-7", "dalil": "Amanah (2 dalil)"},
            "Agustus": {"quran": "Ar Ro'du 1 - Ibrohim 5", "hadist": "Ahkam 23-44", "doa": "Doa pr bp imam 8-13", "surat": "Al-Insiqoq", "dalil": "Mujhidul Muzhid (2 dalil)"},
            "September": {"quran": "Ibrohim 6-15", "hadist": "Ahkam 45-66", "surat": "Al-Mutoffifin", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Oktober": {"quran": "Al Khijer 16 - An Nakel 26", "hadist": "Ahkam 67-88", "surat": "Al-Infitar", "doa": "Asmaul khusna 1-99", "dalil": "Bicara baik (1)"},
            "November": {"quran": "An Nakel 27-83", "hadist": "Ahkam 89-110", "surat": "At-Takwir", "doa": "Doa syukur nikmat", "dalil": "Bicara baik (lanjutan)"},
            "Desember": {"quran": "An Nakel 84-128", "hadist": "Ahkam 111-132", "surat": "Abasa", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Januari": {"quran": "Al Isro' 1-52", "hadist": "Ahkam 133-154", "surat": "An-Naziat", "doa": "Doa mohon ketetapan iman", "dalil": "Sabar (2 dalil)"},
            "Februari": {"quran": "Al Isro' 53-111", "hadist": "Ahkam 155-176", "surat": "An-Naba'", "doa": "Doa ketetapan hati", "dalil": "Pemaaf (2 dalil)"},
            "Maret": {"quran": "Al Kahfi 1-53", "hadist": "Ahkam 177-198", "surat": "Al-Mursalat", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "April": {"quran": "Al Kahfi 54-110", "hadist": "Ahkam 199-220", "surat": "Al-Insan", "doa": "Doa selamat dunia akhirat", "dalil": "Ikhlas (2 dalil)"},
            "Mei": {"quran": "Maryam 1-98", "hadist": "Ahkam 221-230", "surat": "Al-Qiyamah", "doa": "Doa sapu jagad", "dalil": "Istiqomah (2 dalil)"},
            "Juni": {"quran": "Toha 1-82", "hadist": "Ahkam 231-240", "surat": "Al-Mudassir", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
        },
        "Tahun Kedua": {
            "Juli": {"quran": "Al Ambiyak 1-50", "hadist": "Khotbah 1-10", "surat": "Al-Muzammil", "doa": "Doa lindung jelek anggota badan", "dalil": "Amanah (lanjutan)"},
            "Agustus": {"quran": "Al Ambiyak 51-112", "hadist": "Khotbah 11-20", "surat": "Al-Jin", "doa": "Doa masuk pasar", "dalil": "Mujhidul Muzhid (lanjutan)"},
            "September": {"quran": "Al Haj 1-41", "hadist": "Khotbah 21-30", "surat": "Nuh", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Oktober": {"quran": "Al Haj 42-78", "hadist": "Khotbah 31-40", "surat": "Al-Ma'arij", "doa": "Doa menjenguk orang sakit", "dalil": "Bicara baik (lanjutan)"},
            "November": {"quran": "Al Mu'minun 1-61", "hadist": "Khotbah 41-50", "surat": "Al-Haqqoh", "doa": "Doa syukur nikmat", "dalil": "Sabar (lanjutan)"},
            "Desember": {"quran": "Al Mu'minun 62-118", "hadist": "Khotbah 51-60", "surat": "Al-Qolam", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "Januari": {"quran": "An Nur 1-34", "hadist": "Khotbah 61-70", "surat": "Al-Mulk", "doa": "Doa sholat istikhoroh", "dalil": "Pemaaf (lanjutan)"},
            "Februari": {"quran": "An Nur 35-64", "hadist": "Khotbah 71-80", "surat": "At-Tahrim", "doa": "Doa mencari ilmu", "dalil": "Ikhlas (lanjutan)"},
            "Maret": {"quran": "Al Furqon 1-44", "hadist": "Khotbah 81-90", "surat": "At-Tolaq", "doa": "Penderesan", "dalil": "Deres dalil sebelumnya"},
            "April": {"quran": "Al Furqon 45-77", "hadist": "Khotbah 91-100", "surat": "At-Tagobun", "doa": "Doa pengayoman", "dalil": "Istiqomah (lanjutan)"},
            "Mei": {"quran": "As Syu'aro 1-115", "hadist": "Khotbah 101-110", "surat": "Al-Munafiqun", "doa": "Minta surga firdaus", "dalil": "Deres (4 dalil)"},
            "Juni": {"quran": "As Syu'aro 116-227", "hadist": "Khotbah 111-120", "surat": "Al-Jumu'ah", "doa": "Penderesan", "dalil": "Deres (4 dalil)"},
        }
    }
}

st.title("📊 Sistem Evaluasi Kurikulum Generus")

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
