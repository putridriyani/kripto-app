import streamlit as st
from utils.factorization import factorize

st.title("🧮 Faktorisasi Brute Force")

# Input angka n dari pengguna
n = st.number_input("Masukkan nilai n:", min_value=2, step=1)

# Tombol untuk faktorisasi
if st.button("Faktorisasi"):
    factors, exec_time = factorize(n)

    # Menampilkan nilai n yang diinput
    st.subheader("Hasil Faktorisasi:")
    st.write(f"n = {n}")

    # Menampilkan faktor-faktornya
    for i, factor in enumerate(factors, start=1):
        st.write(f"p{i} = {factor}")

    # Menampilkan waktu eksekusi
    st.write(f"⏱ **Waktu Eksekusi:** {exec_time:.6f} detik")
