import streamlit as st
from utils.signcryption_utils import sign_message, encrypt_message, save_encrypted_pdf

st.title("✍️ Tanda Tangan & Enkripsi PDF")

private_key_d = st.text_area("Masukkan Eksponen Privat (d):", "")
public_key_n = st.text_area("Masukkan Modulus (n):", "")
public_key_e = st.text_area("Masukkan Eksponen Publik (e):", "")

uploaded_file = st.file_uploader("📂 Upload File PDF", type=["pdf"])

if st.button("🔒 Tanda Tangani & Enkripsi"):
    if uploaded_file and private_key_d and public_key_n and public_key_e:
        file_bytes = uploaded_file.read()

        try:
            d, n, e = int(private_key_d), int(public_key_n), int(public_key_e)
            signature = sign_message(file_bytes, d, n)
            encrypted_message = encrypt_message(file_bytes, e, n)

            st.success("✅ Berhasil! Pesan telah ditandatangani dan dienkripsi.")
            st.text(f"✍️ Signature: {signature}")

            encrypted_pdf = save_encrypted_pdf(uploaded_file, encrypted_message)
            st.download_button("📥 Download PDF Hasil Enkripsi", data=encrypted_pdf, file_name="encrypted.pdf", mime="application/pdf")
        
        except ValueError:
            st.error("⚠️ Pastikan input kunci dalam bentuk angka yang valid!")

    else:
        st.warning("⚠️ Harap lengkapi semua input sebelum melanjutkan!")
