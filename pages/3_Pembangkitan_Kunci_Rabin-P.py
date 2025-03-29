import streamlit as st
from utils.rabin_p_utils import generate_rabin_keys, save_rabin_keys_as_txt

# 🎨 Load CSS jika ada
def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🚀 Streamlit UI
st.title("🔑 Pembangkitan Kunci Rabin-P")

bit_length = st.number_input("Masukkan bit length (≥ 512):", min_value=512, step=128, value=2048)

if st.button("Generate Kunci Rabin-P"):
    p, q, n = generate_rabin_keys(bit_length)

    st.success("✅ Kunci Rabin-P berhasil dibuat!")
    
    st.text(f"🔢 p (Prime 1): {p}")
    st.text(f"🔢 q (Prime 2): {q}")
    st.text(f"🔢 n (Modulus): {n}")

    # Membuat file unduhan
    key_file = save_rabin_keys_as_txt(p, q, n)
    st.download_button("📥 Download Kunci Rabin-P", data=key_file, file_name="rabin_p_keys.txt", mime="text/plain")
