import streamlit as st
from utils.factorization import factorize

# Panggil load_css() agar styling global tetap berlaku
def load_css():
    with open("static/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("🧮 Faktorisasi Brute Force")

st.markdown("<p style='font-family:Courier; font-size:16px; color:#c43670; margin-bottom: -50px;'>Masukkan nilai n:</p>", unsafe_allow_html=True)
n = st.number_input("", min_value=2, step=1)

# Tombol untuk faktorisasi
if st.button("Faktorisasi"):
    factors, exec_time = factorize(n)

    # Menampilkan nilai n yang diinput
    st.markdown(f"<p style='font-family:Courier; font-size:18px; color:#c43670;'>Hasil Faktorisasi:</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>n = {n}</p>", unsafe_allow_html=True)

    # Menampilkan faktor-faktornya
    for i, factor in enumerate(factors, start=1):
        st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>p{i} = {factor}</p>", unsafe_allow_html=True)

    # Menampilkan waktu eksekusi
    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>⏱ <b>Waktu Eksekusi:</b> {exec_time:.6f} detik</p>", unsafe_allow_html=True)
