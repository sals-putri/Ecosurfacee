# ==========================================================
# ECOSURFACE
# Sistem Pendukung Pemantauan Kualitas Air Permukaan
# Developer : Mahasiswa Politeknik AKA Bogor
# ==========================================================

import streamlit as st
import pandas as pd

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="EcoSurface",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.stApp{
    background: linear-gradient(
        180deg,
        #F5FFF8 0%,
        #EEF8FF 100%
    );
}

.hero{
    background: linear-gradient(
        135deg,
        #2E8B57,
        #1E90FF
    );
    padding:30px;
    border-radius:22px;
    color:white;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0px 6px 18px rgba(0,0,0,0.15);
}

.info-card{
    background:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.10);
    border-left:6px solid #1E90FF;
}

.result-success{
    background:#E8F5E9;
    padding:20px;
    border-radius:18px;
    border-left:8px solid #2E8B57;
    box-shadow:0px 3px 10px rgba(0,0,0,0.10);
}

.result-danger{
    background:#FFEBEE;
    padding:20px;
    border-radius:18px;
    border-left:8px solid #D32F2F;
    box-shadow:0px 3px 10px rgba(0,0,0,0.10);
}

.metric-box{
    background:white;
    padding:15px;
    border-radius:16px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.10);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# DATABASE SAMPLING
# ==========================================================

sampling_data = {

    "pH": {
        "wadah": "Botol PE",
        "volume": "250 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "Segera dianalisis",
        "catatan": "Analisis dilakukan sesegera mungkin setelah sampling."
    },

    "Suhu": {
        "wadah": "Botol PE",
        "volume": "-",
        "pengawet": "Tidak perlu",
        "penyimpanan": "In-situ",
        "holding_time": "Langsung diukur",
        "catatan": "Pengukuran dilakukan langsung di lapangan."
    },

    "TSS": {
        "wadah": "Botol PE",
        "volume": "1000 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Jangan disaring sebelum analisis."
    },

    "TDS": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Simpan dalam kondisi tertutup rapat."
    },

    "DO": {
        "wadah": "Botol Winkler",
        "volume": "300 mL",
        "pengawet": "Fiksasi MnSO4",
        "penyimpanan": "4°C",
        "holding_time": "8 jam",
        "catatan": "Hindari terbentuknya gelembung udara."
    },

    "BOD": {
        "wadah": "Botol PE",
        "volume": "1000 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Analisis secepat mungkin."
    },

    "COD": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Sampel harus segera didinginkan."
    },

    "Nitrat": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Hindari kontaminasi pupuk dan bahan organik."
    },

    "Nitrit": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Simpan dalam pendingin setelah sampling."
    },

    "Amonia": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Hindari paparan sinar matahari langsung."
    },

    "Fosfat": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Kocok perlahan sebelum analisis."
    },

    "Sulfat": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "-"
    },

    "Klorida": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "-"
    },

    "Total Coliform": {
        "wadah": "Botol Steril",
        "volume": "100 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Jaga sterilitas wadah dan sampel."
    },

    "Fecal Coliform": {
        "wadah": "Botol Steril",
        "volume": "100 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Jaga sterilitas selama pengambilan sampel."
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
}

# ==========================================================
# DATABASE BAKU MUTU
# ==========================================================

baku_mutu = {
    "BOD": 3,
    "COD": 25,
    "TSS": 50,
    "TDS": 1000,
    "Nitrat": 10,
    "Nitrit": 0.06,
    "Amonia": 0.5,
    "Fosfat": 0.2,
    "Sulfat": 400,
    "Klorida": 600,
    "Besi (Fe)": 0.3,
    "Mangan (Mn)": 0.1,
    "DO": 4
}

# ==========================================================
# SIDEBAR
# ==========================================================

menu = st.sidebar.radio(
    "📋 Menu Navigasi",
    [
        "🏠 Beranda",
        "🧪 Panduan Sampling",
        "📊 Evaluasi Baku Mutu",
        "ℹ️ Tentang Aplikasi"
        # ==========================================================
# HALAMAN BERANDA
# ==========================================================

if menu == "🏠 Beranda":

    st.markdown("""
    <div class="hero">
        <h1>🌊 EcoSurface</h1>
        <h4>Sistem Pendukung Pemantauan Kualitas Air Permukaan</h4>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="🧪 Parameter Sampling",
            value=len(sampling_data)
        )

    with col2:
        st.metric(
            label="📊 Parameter Baku Mutu",
            value=len(baku_mutu)
        )

    st.write("")

    with st.container():

        st.markdown("""
        <div class="info-card">

        <h3>📖 Tentang EcoSurface</h3>

        EcoSurface merupakan aplikasi pendukung kegiatan
        pemantauan kualitas air permukaan yang membantu pengguna:

        <br><br>

        ✅ Menentukan kebutuhan sampling air permukaan

        <br>

        ✅ Mengetahui jenis wadah dan pengawet yang sesuai

        <br>

        ✅ Menentukan holding time dan kondisi penyimpanan

        <br>

        ✅ Mengevaluasi hasil analisis kualitas air terhadap
        baku mutu yang berlaku

        <br><br>

        Cocok digunakan oleh mahasiswa, laboratorium lingkungan,
        dan praktisi pemantauan kualitas air.

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("📊 Ringkasan Baku Mutu")

    df_baku_mutu = pd.DataFrame({
        "Parameter": list(baku_mutu.keys()),
        "Nilai Baku Mutu": list(baku_mutu.values())
    })

    st.dataframe(
        df_baku_mutu,
        use_container_width=True,
        hide_index=True
    )

# ==========================================================
# HALAMAN PANDUAN SAMPLING
# ==========================================================

elif menu == "🧪 Panduan Sampling":

    st.title("🧪 Panduan Sampling Air Permukaan")

    st.write("""
    Pilih parameter kualitas air yang akan dianalisis.
    Sistem akan menampilkan kebutuhan sampling,
    pengawetan sampel, penyimpanan, dan holding time.
    """)

    parameter = st.selectbox(
        "Pilih Parameter",
        list(sampling_data.keys())
    )

    data = sampling_data[parameter]

    st.write("")

    with st.container():

        st.markdown(f"""
        <div class="info-card">

        <h2>📌 {parameter}</h2>

        <hr>

        🧴 <b>Jenis Wadah</b>

        <br>

        {data["wadah"]}

        <br><br>

        📏 <b>Volume Minimum</b>

        <br>

        {data["volume"]}

        <br><br>

        🧪 <b>Bahan Pengawet</b>

        <br>

        {data["pengawet"]}

        <br><br>

        ❄️ <b>Suhu Penyimpanan</b>

        <br>

        {data["penyimpanan"]}

        <br><br>

        ⏳ <b>Holding Time</b>

        <br>

        {data["holding_time"]}

        <br><br>

        📝 <b>Catatan Tambahan</b>

        <br>

        {data["catatan"]}

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    with st.expander("📚 Informasi Tambahan"):

        st.markdown(f"""
        *Parameter yang dipilih:* {parameter}

        Pastikan pengambilan sampel dilakukan sesuai prosedur
        dan menggunakan wadah yang sesuai agar hasil analisis
        laboratorium tetap representatif.
        """) 
        # ==========================================================
# HALAMAN EVALUASI BAKU MUTU
# ==========================================================

elif menu == "📊 Evaluasi Baku Mutu":

    st.title("📊 Evaluasi Baku Mutu")

    st.write("""
    Masukkan hasil analisis laboratorium untuk mengetahui
    apakah parameter tersebut memenuhi baku mutu atau tidak.
    """)

    parameter = st.selectbox(
        "Pilih Parameter",
        list(baku_mutu.keys())
    )

    nilai = st.number_input(
        "Masukkan Hasil Analisis",
        min_value=0.0,
        value=0.0,
        step=0.01
    )

    st.write("")

    if st.button("🔍 Evaluasi", use_container_width=True):

        standar = baku_mutu[parameter]

        # ==========================================
        # LOGIKA KHUSUS DO
        # ==========================================

        if parameter == "DO":

            memenuhi = nilai >= standar

        else:

            memenuhi = nilai <= standar

        selisih = abs(nilai - standar)

        st.write("")

        if memenuhi:

            st.markdown(f"""
            <div class="result-success">

            <h2>✅ MEMENUHI BAKU MUTU</h2>

            <hr>

            <b>Parameter</b><br>
            {parameter}

            <br><br>

            <b>Hasil Analisis</b><br>
            {nilai}

            <br><br>

            <b>Nilai Baku Mutu</b><br>
            {standar}

            <br><br>

            <b>Selisih Nilai</b><br>
            {selisih}

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="result-danger">

            <h2>❌ TIDAK MEMENUHI BAKU MUTU</h2>

            <hr>

            <b>Parameter</b><br>
            {parameter}

            <br><br>

            <b>Hasil Analisis</b><br>
            {nilai}

            <br><br>

            <b>Nilai Baku Mutu</b><br>
            {standar}

            <br><br>

            <b>Selisih Nilai</b><br>
            {selisih}

            </div>
            """, unsafe_allow_html=True)

        st.write("")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Hasil Analisis",
                nilai
            )

        with col2:
            st.metric(
                "Baku Mutu",
                standar
            )

        with col3:
            st.metric(
                "Selisih",
                round(selisih, 3)
            )

# ==========================================================
# HALAMAN TENTANG APLIKASI
# ==========================================================

elif menu == "ℹ️ Tentang Aplikasi":

    st.title("ℹ️ Tentang Aplikasi")

    with st.container():

        st.markdown("""
        <div class="info-card">

        <h2>🌊 EcoSurface</h2>

        <hr>

        <b>Deskripsi</b>

        <br><br>

        Aplikasi pendukung kegiatan pemantauan kualitas air
        permukaan yang membantu menentukan kebutuhan sampling,
        pengawetan contoh, penyimpanan, holding time,
        dan evaluasi hasil analisis berdasarkan baku mutu.

        <br><br>

        <b>Teknologi</b>

        <ul>
            <li>Python</li>
            <li>Streamlit</li>
            <li>Pandas</li>
        </ul>

        <b>Versi</b>

        <br>

        1.0

        <br><br>

        <b>Developer</b>

        <br>

        Mahasiswa Politeknik AKA Bogor

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    with st.expander("🎯 Tujuan Pengembangan"):

        st.write("""
        Aplikasi ini dikembangkan sebagai media pembelajaran
        dan pendukung kegiatan pemantauan kualitas air
        permukaan bagi mahasiswa maupun praktisi lingkungan.
        """)

# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.write("")

st.markdown(
    """
    <center>
    <small>
    🌿 EcoSurface v1.0 | Sistem Pendukung Pemantauan Kualitas Air Permukaan
    </small>
    </center>
    """,
    unsafe_allow_html=True
)
    ]
)
