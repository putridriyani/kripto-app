import streamlit as st
from Crypto.Util import number
from PyPDF2 import PdfReader
from fpdf import FPDF
from io import BytesIO
import base64



st.title("🔏 Tanda Tangan & Enkripsi")

# Form Input Kunci RSA
st.subheader("Masukkan Kunci Publik RSA:")
n = st.text_area("Masukkan nilai n (modulus):")
e = st.text_area("Masukkan nilai e (eksponen publik):")

# Form Input Kunci Rabin-P
st.subheader("Masukkan Kunci Privat Rabin-P:")
p = st.text_area("Masukkan nilai p (bilangan prima 1):")
q = st.text_area("Masukkan nilai q (bilangan prima 2):")

# File PDF yang akan dienkripsi
uploaded_file = st.file_uploader("Unggah file PDF untuk dienkripsi:", type=["pdf"])

# Fungsi Tanda Tangan dengan Rabin-P
def sign_with_rabin(message, p, q):
    """Tanda tangan digital dengan algoritma Rabin-P."""
    n = p * q
    hashed = abs(hash(message)) % n
    signature = pow(hashed, 2, n)
    return signature

# Fungsi Enkripsi dengan RSA
def encrypt_with_rsa(message, n, e):
    """Enkripsi pesan dengan RSA menggunakan kunci publik (n, e)."""
    message_int = int.from_bytes(message.encode(), 'big')
    encrypted_int = pow(message_int, e, n)
    return encrypted_int

# Fungsi Menyimpan ke PDF
def save_encrypted_pdf(encrypted_text):
    """Simpan hasil enkripsi sebagai PDF dengan encoding yang benar."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Encoding hasil enkripsi sebagai Base64 agar aman disimpan di PDF
    encoded_text = base64.b64encode(encrypted_text.encode()).decode()

    # Pecah teks panjang agar tidak melebihi lebar halaman PDF
    lines = [encoded_text[i:i+100] for i in range(0, len(encoded_text), 100)]
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True)

    buffer = BytesIO()
    pdf.output(buffer, 'S')  # Simpan dalam memori
    buffer.seek(0)
    return buffer


if st.button("🔐 Tanda Tangani & Enkripsi"):
    if uploaded_file and n and e and p and q:
        try:
            # Konversi input ke angka
            n, e, p, q = int(n), int(e), int(p), int(q)

            # Membaca file PDF langsung dari uploaded_file
            reader = PdfReader(uploaded_file)

            # Ekstrak teks dari PDF
            pdf_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

            if not pdf_text:
                st.error("⚠️ File PDF kosong atau tidak memiliki teks yang dapat diekstrak!")
                st.stop()

            # DEBUG: Cek isi PDF sebelum diproses
            st.write("📄 **Isi PDF yang diekstrak:**")
            st.code(pdf_text[:500])  # Tampilkan sebagian teks (max 500 karakter)

            # Tanda tangan dengan Rabin-P
            signature = sign_with_rabin(pdf_text, p, q)

            # DEBUG: Cek hasil tanda tangan
            st.write("✍️ **Signature (Tanda Tangan):**", signature)

            # Gabungkan teks PDF dengan tanda tangan
            signed_text = pdf_text + "\n\n[Signature]: " + str(signature)

            # Enkripsi dengan RSA
            encrypted_int = encrypt_with_rsa(signed_text, n, e)

            # DEBUG: Cek hasil enkripsi
            st.write("🔒 **Hasil Enkripsi (Angka Besar):**", encrypted_int)

            # Konversi angka besar ke teks (agar bisa disimpan ke PDF)
            encrypted_text = str(encrypted_int)

            # Simpan sebagai PDF terenkripsi
            encrypted_pdf = save_encrypted_pdf(encrypted_text)

            st.success("✅ Berhasil ditandatangani dan dienkripsi!")
            st.download_button("📥 Unduh PDF Terenkripsi", data=encrypted_pdf, file_name="encrypted.pdf", mime="application/pdf")

        except Exception as err:
            st.error(f"❌ Terjadi kesalahan: {err}")

    else:
        st.warning("⚠️ Harap masukkan semua kunci dan unggah file PDF!")


