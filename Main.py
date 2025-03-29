import streamlit as st
import os


def load_css():
    with open("static/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil fungsi ini agar semua halaman memakai CSS
load_css()

st.title("🔑 Aplikasi Kriptografi dengan RSA Signature & Rabin-P")
st.write("Silakan pilih menu di sidebar untuk memulai.")
