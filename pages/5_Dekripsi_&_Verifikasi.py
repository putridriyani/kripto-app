import streamlit as st
from fpdf import FPDF
import hashlib
from io import BytesIO
import PyPDF2

# 📌 Fungsi untuk verifikasi tanda tangan
def verify_signature(message, signature, public_key, n):
    """Memverifikasi tanda tangan digital dengan RSA Signature (angka besar)."""
    hashed = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    verified_hash = pow(signature, public_key, n)  # Dekripsi tanda tangan
    return hashed == verified_hash

# 📌 Fungsi untuk mendekripsi pesan dengan Rabin-P
def decrypt_message(encrypted_message, p, q):
    """Mendekripsi pesan dengan algoritma Rabin-P (angka besar)."""
    n = p * q  # Modulus Rabin-P
    decrypted_int = pow(encrypted_message, 2, n)  # Dekripsi dengan eksponen privat
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
    return decrypted_bytes.decode(errors="ignore")  # Konversi kembali ke teks

# 📌 Fungsi untuk membaca data dari PDF terenkripsi
def read_pdf(uploaded_file):
    """Membaca tanda tangan dan pesan terenkripsi dari file PDF."""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        # Ekstrak tanda tangan dan enkripsi dari teks PDF
        lines = text.split("\n")
        signature = int(lines[1].split(":")[1].strip())  # Ambil tanda tangan dari PDF
        encrypted_message = int(lines[3].split(":")[1].strip())  # Ambil pesan terenkripsi
        return signature, encrypted_message
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat membaca PDF: {e}")
        return None, None

# 📌 UI Streamlit
st.title("🔓✍️ Dekripsi & Verifikasi")

uploaded_file = st.file_uploader("📂 Unggah file hasil enkripsi (PDF)", type=["pdf"])

# Form Input Kunci RSA
st.subheader("Masukkan Kunci Publik RSA:")
n_rsa = st.text_area("Masukkan nilai **n** dari RSA:", height=100)
public_key_rsa = st.text_area("Masukkan eksponen publik **e** dari RSA:", height=100)

# Form Input Kunci Rabin-P
st.subheader("Masukkan Kunci Privat Rabin-P:")
p_rabin = st.text_area("Masukkan nilai **p** dari Rabin-P:", height=100)
q_rabin = st.text_area("Masukkan nilai **q** dari Rabin-P:", height=100)

if st.button("🔓 Dekripsi & Verifikasi"):
    if uploaded_file and n_rsa and public_key_rsa and p_rabin and q_rabin:
        try:
            # 🔹 Konversi input ke angka besar
            n_rsa = int(n_rsa.strip())
            public_key_rsa = int(public_key_rsa.strip())
            p_rabin = int(p_rabin.strip())
            q_rabin = int(q_rabin.strip())

            # 🔹 Baca tanda tangan & pesan terenkripsi dari PDF
            signature, encrypted_message = read_pdf(uploaded_file)

            if signature is None or encrypted_message is None:
                st.warning("⚠️ Gagal membaca file PDF!")
            else:
                # 🔹 Dekripsi pesan
                decrypted_message = decrypt_message(encrypted_message, p_rabin, q_rabin)

                # 🔹 Verifikasi tanda tangan
                is_verified = verify_signature(decrypted_message, signature, public_key_rsa, n_rsa)

                # 🔹 Tampilkan hasil
                st.subheader("✅ Hasil:")
                st.text_area("📜 Pesan Asli:", decrypted_message, height=200)
                st.write(f"🔍 Hasil Verifikasi: {'✅ Valid' if is_verified else '❌ Tidak Valid'}")
        except ValueError:
            st.error("❌ Pastikan semua kunci dalam format angka yang valid!")
    else:
        st.warning("⚠️ Mohon isi semua input dengan benar!")
