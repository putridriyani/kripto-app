import streamlit as st
from utils.signcryption_utils import sign_message, encrypt_message, save_encrypted_pdf

# Panggil load_css() agar styling global tetap berlaku
def load_css():
    with open("static/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("✍️ Tanda Tangan & Enkripsi PDF")

# Eksponen Privat
st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670;margin-bottom: -50px;'>Masukkan Eksponen Privat (d):</p>", unsafe_allow_html=True)
private_key_d = st.text_area("‎ ", key="private_key_d")  # Spasi khusus (invisible)

# Modulus
st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670;margin-bottom: -50px;'>Masukkan Modulus (n):</p>", unsafe_allow_html=True)
public_key_n = st.text_area("‎ ", key="public_key_n")  # Spasi khusus (invisible)

# Eksponen Publik
st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670;margin-bottom:-10;margin-bottom: -50px;'>Masukkan Eksponen Publik (e):</p>", unsafe_allow_html=True)
public_key_e = st.text_area("‎ ", key="public_key_e")  # Spasi khusus (invisible)

# Upload File PDF
st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670; margin-bottom: -10px;'>📂 Upload File PDF:</p>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("‎ ", type=["pdf"], key="uploaded_file")  # Spasi khusus (invisible)


if st.button("🔒 Tanda Tangani & Enkripsi"):
    if uploaded_file and private_key_d and public_key_n and public_key_e:
        file_bytes = uploaded_file.read()

        try:
            d, n, e = int(private_key_d), int(public_key_n), int(public_key_e)
            signature = sign_message(file_bytes, d, n)
            encrypted_message = encrypt_message(file_bytes, e, n)

            st.markdown("<p style='font-family:Courier; font-size:18px; color:#c43670;'>✅ Berhasil! Pesan telah ditandatangani dan dienkripsi.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-family:Courier; font-size:18px; color:#c43670;'>✍️ Signature: {signature}</p>", unsafe_allow_html=True)

            encrypted_pdf = save_encrypted_pdf(uploaded_file, encrypted_message)
            st.download_button("📥 Download PDF Hasil Enkripsi", data=encrypted_pdf, file_name="encrypted.pdf", mime="application/pdf")
        
        except ValueError:
            st.markdown("<p style='font-family:Courier; font-size:18px; color:red;'>⚠️ Pastikan input kunci dalam bentuk angka yang valid!</p>", unsafe_allow_html=True)

    else:
        st.markdown("<p style='font-family:Courier; font-size:18px; color:orange;'>⚠️ Harap lengkapi semua input sebelum melanjutkan!</p>", unsafe_allow_html=True)
