import streamlit as st
from utils.rsa_signature_utils import generate_rsa_signature_keys, save_keys_as_txt

 
def load_css():
    with open("static/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("🔑 Pembangkitan Kunci RSA Signature")

st.markdown("<p style='font-family:Courier; font-size:16px; color:#c43670; margin-bottom: -50px;'>Masukkan bit length (≥ 512):</p>", unsafe_allow_html=True)

bit_length = st.number_input("", min_value=512, step=128, value=2048)

if st.button("🔑 Generate Kunci RSA Signature"):
    n, e, d = generate_rsa_signature_keys(bit_length)

    st.markdown("<p style='font-family:Courier; font-size:18px; color:green;'>✅ Kunci RSA Signature berhasil dibuat!</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>🔢 n (Modulus): {n}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>🔢 e (Eksponen Publik): {e}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>🔢 d (Eksponen Privat): {d}</p>", unsafe_allow_html=True)

    key_file = save_keys_as_txt(n, e, d)
    
    st.markdown(
        """
        <style>
        .download-button button {
            font-family: Courier !important;
            font-size: 16px !important;
            color: white !important;
            background-color: #fbd9e5 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.download_button("📥 Download Kunci RSA Signature", data=key_file, file_name="rsa_signature_keys.txt", mime="text/plain", key="download_rsa")
