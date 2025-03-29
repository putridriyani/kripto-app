import streamlit as st
from utils.rsa_signature_utils import generate_rsa_signature_keys, save_keys_as_txt

# 🎨 Load CSS jika ada
def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🚀 Streamlit UI
st.title("🔑 Pembangkitan Kunci RSA Signature")

bit_length = st.number_input("Masukkan bit length (≥ 512):", min_value=512, step=128, value=2048)

if st.button("Generate Kunci RSA Signature"):
    n, e, d = generate_rsa_signature_keys(bit_length)

    st.success("✅ Kunci RSA Signature berhasil dibuat!")
    
    st.text(f"🔢 n (Modulus): {n}")
    st.text(f"🔢 e (Eksponen Publik): {e}")
    st.text(f"🔢 d (Eksponen Privat): {d}")

    # Membuat file unduhan
    key_file = save_keys_as_txt(n, e, d)
    st.download_button("📥 Download Kunci RSA Signature", data=key_file, file_name="rsa_signature_keys.txt", mime="text/plain")
