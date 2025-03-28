import streamlit as st
from utils.rabin_p_utils import generate_rabin_keys_as_numbers

st.title("🔑 Pembangkitan Kunci Rabin-P")

bit_length = st.number_input("Masukkan bit length (≥ 512):", min_value=512, step=128, value=2048)

if st.button("Generate Kunci Rabin-P"):
    p, q, n = generate_rabin_keys_as_numbers(bit_length)
    
    st.success("Kunci Rabin-P berhasil dibuat!")
    st.text(f"p: {p}")
    st.text(f"q: {q}")
    st.text(f"n (Modulus): {n}")
