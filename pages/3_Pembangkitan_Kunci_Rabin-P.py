import streamlit as st
from utils.rabin_p_utils import generate_rabin_keys, save_rabin_keys_as_txt

# Panggil load_css() agar styling global tetap berlaku
def load_css():
    with open("static/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# 🚀 Streamlit UI
st.title("🔑 Pembangkitan Kunci Rabin-P")

st.markdown("<p style='font-family:Courier; font-size:16px; color:#c43670; margin-bottom: -50px;'>Masukkan bit length (≥ 512):</p>", unsafe_allow_html=True)

bit_length = st.number_input("", min_value=512, step=128, value=2048)

if st.button("🔑 Generate Kunci Rabin-P"):
    p, q, n = generate_rabin_keys(bit_length)

    st.markdown("<p style='font-family:Courier; font-size:18px; color:green;'>✅ Kunci Rabin-P berhasil dibuat!</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>🔢 p (Prime 1): {p}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>🔢 q (Prime 2): {q}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family:Courier; font-size:16px; color:#c43670;'>🔢 n (Modulus): {n}</p>", unsafe_allow_html=True)


    # Membuat file unduhan
    key_file = save_rabin_keys_as_txt(p, q, n)
    st.download_button("📥 Download Kunci Rabin-P", data=key_file, file_name="rabin_p_keys.txt", mime="text/plain")