import hashlib
from Crypto.Util import number
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter

def sign_message(message, private_key_d, n):
    """Membuat tanda tangan digital menggunakan RSA Signature"""
    hashed = int(hashlib.sha256(message).hexdigest(), 16)
    signature = pow(hashed, private_key_d, n)
    return signature

def encrypt_message(message, public_key_e, n):
    """Mengenkripsi pesan menggunakan RSA"""
    message_int = int.from_bytes(message, byteorder='big')
    encrypted_message = pow(message_int, public_key_e, n)
    return encrypted_message

def decrypt_message(encrypted_message, private_key_d, n):
    """Mendekripsi pesan menggunakan RSA"""
    decrypted_int = pow(encrypted_message, private_key_d, n)
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
    return decrypted_bytes

def verify_signature(message, signature, public_key_e, n):
    """Memverifikasi tanda tangan digital"""
    hashed = int(hashlib.sha256(message).hexdigest(), 16)
    calculated_hash = pow(signature, public_key_e, n)
    return hashed == calculated_hash

def save_encrypted_pdf(original_pdf, encrypted_message):
    """Menyimpan hasil enkripsi dalam file PDF"""
    output_pdf = BytesIO()
    writer = PdfWriter()
    
    encrypted_data = str(encrypted_message).encode()
    
    writer.add_blank_page(width=300, height=300)  # Tambahkan halaman kosong
    writer.write(output_pdf)

    output_pdf.write(encrypted_data)  # Simpan hasil enkripsi dalam PDF
    output_pdf.seek(0)
    
    return output_pdf
