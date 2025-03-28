import streamlit as st
from utils.rsa_utils import generate_rsa_keys_as_numbers

st.title("🔑 Pembangkitan Kunci RSA")

bit_length = st.number_input("Masukkan bit length (≥ 512):", min_value=512, step=128, value=2048)

if st.button("Generate Kunci RSA"):
    try:
        n, e, d = generate_rsa_keys_as_numbers(bit_length)
        st.success("✅ Kunci RSA berhasil dibuat!")
        st.text_area("🔢 n (Modulus)", value=str(n), height=100)
        st.text_area("🔢 e (Eksponen Publik)", value=str(e), height=100)
        st.text_area("🔢 d (Eksponen Privat)", value=str(d), height=100)
    except Exception as err:
        st.error(f"❌ Terjadi kesalahan: {err}")
