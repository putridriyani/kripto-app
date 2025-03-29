import streamlit as st
from utils.signcryption_utils import decrypt_message, verify_signature
from io import BytesIO

st.title("🔓 Dekripsi & Verifikasi PDF")

private_key_d = st.text_area("Masukkan Eksponen Privat (d):", "")
public_key_n = st.text_area("Masukkan Modulus (n):", "")
public_key_e = st.text_area("Masukkan Eksponen Publik (e):", "")

signature_input = st.text_area("Masukkan Signature (Angka Besar):", "")
uploaded_file = st.file_uploader("📂 Upload File PDF Terenkripsi", type=["pdf"])

if st.button("🔓 Dekripsi & Verifikasi"):
    if private_key_d and public_key_n and public_key_e and signature_input and uploaded_file:
        file_bytes = uploaded_file.read()

        try:
            d, n, e = int(private_key_d), int(public_key_n), int(public_key_e)
            signature = int(signature_input)

            decrypted_message = decrypt_message(int.from_bytes(file_bytes, byteorder='big'), d, n)
            is_valid = verify_signature(decrypted_message, signature, e, n)

            if is_valid:
                st.success("✅ Tanda tangan valid! Pesan berhasil didekripsi.")

                decrypted_pdf = BytesIO(decrypted_message)
                decrypted_pdf.seek(0)

                st.download_button("📥 Download File PDF Asli", data=decrypted_pdf, file_name="decrypted.pdf", mime="application/pdf")
            else:
                st.error("❌ Tanda tangan tidak valid! Data mungkin telah diubah.")

        except ValueError:
            st.error("⚠️ Pastikan input dalam bentuk angka yang valid!")

    else:
        st.warning("⚠️ Harap lengkapi semua input sebelum melanjutkan!")
