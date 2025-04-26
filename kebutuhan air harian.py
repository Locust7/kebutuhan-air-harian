import streamlit as st

st.set_page_config(page_title="Kebutuhan Air Harian", layout="centered")

st.title("💧 Kebutuhan Air Harian")
st.write("Hitung berapa liter air yang kamu butuhkan setiap hari berdasarkan berat badan dan aktivitas.")

# Input user
berat = st.number_input("Masukkan berat badan kamu (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("Pilih tingkat aktivitas kamu:", 
                         ["Ringan", "Sedang", "Berat"])

# Fungsi hitung
def hitung_air(berat, aktivitas):
    dasar = berat * 30
    tambahan = {"Ringan": 0, "Sedang": 300, "Berat": 600}
    total_ml = dasar + tambahan[aktivitas]
    return total_ml / 1000  # Liter

# Hasil
if st.button("Hitung"):
    if berat > 0:
        hasil = hitung_air(berat, aktivitas)
        st.success(f"Kamu butuh sekitar *{hasil:.2f} liter air* per hari.")
    else:
        st.warning("Masukkan berat badan yang valid.")

st.markdown("---")
st.caption("Proyek Streamlit oleh [Kelompok 7]")
