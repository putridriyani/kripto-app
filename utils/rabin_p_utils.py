from Crypto.Util import number
from io import BytesIO

def generate_rabin_keys(bit_length=2048):
    """Membuat pasangan kunci Rabin-P dalam bentuk angka besar."""
    p = number.getPrime(bit_length // 2)  # Bilangan prima pertama
    q = number.getPrime(bit_length // 2)  # Bilangan prima kedua
    n = p * q  # Modulus

    return p, q, n

def save_rabin_keys_as_txt(p, q, n):
    """Menyimpan kunci Rabin-P ke file TXT untuk diunduh."""
    output = f"p (Prime 1): {p}\n\n"
    output += f"q (Prime 2): {q}\n\n"
    output += f"n (Modulus): {n}\n"

    # Simpan ke BytesIO untuk diunduh
    file = BytesIO()
    file.write(output.encode())
    file.seek(0)
    return file
