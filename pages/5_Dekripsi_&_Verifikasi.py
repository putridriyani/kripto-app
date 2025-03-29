import streamlit as st
from utils.signcryption_utils import decrypt_message, verify_signature
from io import BytesIO

# Panggil load_css() agar styling global tetap berlaku
def load_css():
    with open("static/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("🔓 Dekripsi & Verifikasi PDF")

# Input teks dengan Markdown inline
st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670; margin-bottom: -50px;'>Masukkan Eksponen Privat (d):</p>", unsafe_allow_html=True)
private_key_d = st.text_area("", key="private_key_d")

st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670; margin-bottom: -50px;'>Masukkan Modulus (n):</p>", unsafe_allow_html=True)
public_key_n = st.text_area("", key="public_key_n")

st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670; margin-bottom: -50px;'>Masukkan Eksponen Publik (e):</p>", unsafe_allow_html=True)
public_key_e = st.text_area("", key="public_key_e")

st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670; margin-bottom: -50px;'>Masukkan Signature (Angka Besar):</p>", unsafe_allow_html=True)
signature_input = st.text_area("", key="signature_input")

st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670; margin-bottom: -10px;'>📂 Upload File PDF Terenkripsi:</p>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], key="uploaded_file")

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
