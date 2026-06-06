import streamlit as st

# =====================================================

# KONFIGURASI HALAMAN

# =====================================================

st.set_page_config(
page_title="EcoSurface",
page_icon="🌊",
layout="wide"
)

# =====================================================

# DATABASE PARAMETER SAMPLING

# =====================================================

sampling_data = {

'''
"pH": {
    "wadah": "Botol PE",
    "volume": "100 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "Analisis langsung",
    "holding_time": "15 menit",
    "catatan": "Diukur langsung di lapangan."
},

"Suhu": {
    "wadah": "In-situ",
    "volume": "-",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "Analisis langsung",
    "holding_time": "Segera",
    "catatan": "Gunakan termometer terkalibrasi."
},

"TSS": {
    "wadah": "Botol PE",
    "volume": "1000 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "7 hari",
    "catatan": "Hindari pengendapan sebelum analisis."
},

"TDS": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "7 hari",
    "catatan": "Simpan dalam kondisi tertutup."
},

"DO": {
    "wadah": "Botol Winkler",
    "volume": "300 mL",
    "pengawet": "MnSO4 dan Alkali Iodida",
    "penyimpanan": "4°C",
    "holding_time": "8 jam",
    "catatan": "Hindari gelembung udara."
},

"BOD": {
    "wadah": "Botol BOD",
    "volume": "1000 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "48 jam",
    "catatan": "Segera didinginkan setelah sampling."
},

"COD": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "H2SO4 hingga pH < 2",
    "penyimpanan": "4°C",
    "holding_time": "28 hari",
    "catatan": "Sampel segera didinginkan."
},

"Nitrat": {
    "wadah": "Botol PE",
    "volume": "250 mL",
    "pengawet": "H2SO4 hingga pH < 2",
    "penyimpanan": "4°C",
    "holding_time": "28 hari",
    "catatan": "Hindari kontaminasi pupuk."
},

"Nitrit": {
    "wadah": "Botol PE",
    "volume": "250 mL",
    "pengawet": "Pendinginan 4°C",
    "penyimpanan": "4°C",
    "holding_time": "48 jam",
    "catatan": "Analisis sesegera mungkin."
},

"Amonia": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "H2SO4 hingga pH < 2",
    "penyimpanan": "4°C",
    "holding_time": "28 hari",
    "catatan": "Simpan dalam wadah tertutup."
},

"Fosfat": {
    "wadah": "Botol PE",
    "volume": "250 mL",
    "pengawet": "Pendinginan 4°C",
    "penyimpanan": "4°C",
    "holding_time": "48 jam",
    "catatan": "Hindari kontaminasi deterjen."
},

"Sulfat": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "28 hari",
    "catatan": "Pastikan wadah bersih."
},

"Klorida": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "28 hari",
    "catatan": "Hindari kontaminasi garam."
},

"Total Coliform": {
    "wadah": "Botol Steril",
    "volume": "250 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "6 jam",
    "catatan": "Jangan membuka wadah sebelum sampling."
},

"Fecal Coliform": {
    "wadah": "Botol Steril",
    "volume": "250 mL",
    "pengawet": "Tidak diperlukan",
    "penyimpanan": "4°C",
    "holding_time": "6 jam",
    "catatan": "Analisis mikrobiologi sesegera mungkin."
},

"Besi (Fe)": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "HNO3 hingga pH < 2",
    "penyimpanan": "4°C",
    "holding_time": "6 bulan",
    "catatan": "Gunakan wadah bebas logam."
},

"Mangan (Mn)": {
    "wadah": "Botol PE",
    "volume": "500 mL",
    "pengawet": "HNO3 hingga pH < 2",
    "penyimpanan": "4°C",
    "holding_time": "6 bulan",
    "catatan": "Gunakan wadah bebas logam."
}
'''

}

# =====================================================

# DATA BAKU MUTU

# =====================================================

baku_mutu = {
"BOD": 3,"mg/L"
"COD": 25,"mg/L"
"TSS": 50,"mg/L"
"TDS": 1000,"mg/L"
"Nitrat": 10,"mg/L"
"Nitrit": 0.06,"mg/L"
"Amonia": 0.5,"mg/L"
"Fosfat": 0.2,"mg/L"
"Sulfat": 400,"mg/L"
"Klorida": 600,"mg/L"
"Besi (Fe)": 0.3,"mg/L"
"Mangan (Mn)": 0.1,"mg/L"
"DO": 4,"mg/L"
}

# =====================================================

# CUSTOM CSS

# =====================================================

st.markdown("""

<style>

.main {
    background-color: #F5F9FA;
}

.hero-box {
    background: linear-gradient(
        90deg,
        #2E8B57,
        #1E90FF
    );
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.custom-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.custom-card:hover {
    transform: translateY(-3px);
    transition: 0.3s;
}

.success-card {
    background-color: #E8F5E9;
    border-left: 8px solid green;
    padding: 20px;
    border-radius: 12px;
}

.danger-card {
    background-color: #FFEBEE;
    border-left: 8px solid red;
    padding: 20px;
    border-radius: 12px;
}

.sidebar .sidebar-content {
    background-color: #FFFFFF;
}

</style>

""", unsafe_allow_html=True)

# =====================================================

# SIDEBAR MENU

# =====================================================

st.sidebar.title("🌊 EcoSurface")

menu = st.sidebar.radio(
"Pilih Menu",
[
"🏠 Beranda",
"🧪 Panduan Sampling",
"📊 Evaluasi Baku Mutu",
"ℹ️ Tentang Aplikasi"
]
)

# =====================================================

# HALAMAN BERANDA

# =====================================================

if menu == "🏠 Beranda":

```
st.markdown("""
<div class="hero-box">
    <h1>🌊 EcoSurface</h1>
    <h3>Sistem Pendukung Pemantauan Kualitas Air Permukaan</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Jumlah Parameter Sampling",
        value=len(sampling_data)
    )

with col2:
    st.metric(
        label="Jumlah Parameter Baku Mutu",
        value=len(baku_mutu)
    )

st.markdown("""
<div class="custom-card">

<h3>📖 Tentang EcoSurface</h3>

EcoSurface merupakan aplikasi pendukung kegiatan
pemantauan kualitas air permukaan yang membantu
pengguna menentukan kebutuhan sampling,
pengawetan contoh, penyimpanan, holding time,
serta evaluasi hasil analisis terhadap baku mutu.

Aplikasi ini dirancang sebagai media pembelajaran,
praktikum, dan pendamping kegiatan monitoring
kualitas lingkungan.

</div>
""", unsafe_allow_html=True)

with st.expander("🌱 Manfaat Aplikasi"):
    st.write("""
    ✅ Membantu menentukan kebutuhan sampling

    ✅ Menyediakan informasi pengawetan sampel

    ✅ Menampilkan holding time setiap parameter

    ✅ Mengevaluasi hasil analisis terhadap baku mutu

    ✅ Mendukung kegiatan praktikum lingkungan
    """)
```
# =====================================================

# PANDUAN SAMPLING

# =====================================================

elif menu == "🧪 Panduan Sampling":

```
st.title("🧪 Panduan Sampling Air Permukaan")

parameter = st.selectbox(
    "Pilih Parameter",
    list(sampling_data.keys())
)

data = sampling_data[parameter]

st.markdown(
    f"""
    <div class="custom-card">

    <h2>🧪 {parameter}</h2>

    <hr>

    <p><b>🧴 Jenis Wadah</b><br>
    {data['wadah']}</p>

    <p><b>📦 Volume Minimum</b><br>
    {data['volume']}</p>

    <p><b>⚗️ Bahan Pengawet</b><br>
    {data['pengawet']}</p>

    <p><b>❄️ Suhu Penyimpanan</b><br>
    {data['penyimpanan']}</p>

    <p><b>⏳ Holding Time</b><br>
    {data['holding_time']}</p>

    <p><b>📝 Catatan Tambahan</b><br>
    {data['catatan']}</p>

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.info(
        f"""
        Parameter yang dipilih:
        {parameter}
        """
    )

with col2:
    st.success(
        """
        Panduan sampling berhasil dimuat
        """
    )

with st.expander("📚 Petunjuk Penggunaan"):
    st.write("""
    1. Pilih parameter yang ingin dianalisis.
    2. Baca kebutuhan wadah sampling.
    3. Perhatikan bahan pengawet yang diperlukan.
    4. Simpan sampel sesuai suhu penyimpanan.
    5. Pastikan analisis dilakukan sebelum holding time berakhir.
    """)
```
# =====================================================

# EVALUASI BAKU MUTU

# =====================================================

elif menu == "📊 Evaluasi Baku Mutu":

```
st.title("📊 Evaluasi Baku Mutu")

parameter = st.selectbox(
    "Pilih Parameter",
    list(baku_mutu.keys())
)

hasil_analisis = st.number_input(
    "Masukkan Hasil Analisis",
    min_value=0.0,
    value=0.0,
    step=0.01
)

if st.button("🔍 Evaluasi"):

    nilai_baku_mutu = baku_mutu[parameter]

    if parameter == "DO":

        memenuhi = hasil_analisis >= nilai_baku_mutu
        selisih = hasil_analisis - nilai_baku_mutu

    else:

        memenuhi = hasil_analisis <= nilai_baku_mutu
        selisih = nilai_baku_mutu - hasil_analisis

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Hasil Analisis",
            hasil_analisis
        )

    with col2:
        st.metric(
            "Nilai Baku Mutu",
            nilai_baku_mutu
        )

    with col3:
        st.metric(
            "Selisih",
            round(selisih, 3)
        )

    st.write("")

    if memenuhi:

        st.markdown(
            """
            <div class="success-card">

            <h2>✅ MEMENUHI BAKU MUTU</h2>

            Nilai parameter masih berada
            dalam rentang yang diizinkan.

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="danger-card">

            <h2>❌ TIDAK MEMENUHI BAKU MUTU</h2>

            Nilai parameter telah melewati
            batas baku mutu yang berlaku.

            </div>
            """,
            unsafe_allow_html=True
        )

with st.expander("📖 Keterangan Evaluasi"):

    st.write("""
    Parameter maksimum:

    • BOD
    • COD
    • TSS
    • TDS
    • Nitrat
    • Nitrit
    • Amonia
    • Fosfat
    • Sulfat
    • Klorida
    • Besi (Fe)
    • Mangan (Mn)

    Status memenuhi jika nilai ≤ baku mutu.
    """)

    st.write("""
    Parameter minimum:

    • DO

    Status memenuhi jika nilai ≥ baku mutu.
    """)
```

# =====================================================

# TENTANG APLIKASI

# =====================================================

elif menu == "ℹ️ Tentang Aplikasi":

```
st.title("ℹ️ Tentang Aplikasi")

st.markdown(
    """
    <div class="custom-card">

    <h2>🌊 EcoSurface</h2>

    <p>
    Aplikasi pendukung kegiatan pemantauan kualitas
    air permukaan yang membantu menentukan kebutuhan
    sampling, pengawetan contoh, penyimpanan,
    holding time, dan evaluasi hasil analisis
    berdasarkan baku mutu.
    </p>

    <hr>

    <h4>💻 Teknologi</h4>

    <ul>
    <li>Python</li>
    <li>Streamlit</li>
    </ul>

    <h4>📦 Versi</h4>

    <p>1.0</p>

    <h4>👨‍🎓 Developer</h4>

    <p>Mahasiswa Politeknik AKA Bogor</p>

    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    "Terima kasih telah menggunakan EcoSurface 🌱"
)
```
