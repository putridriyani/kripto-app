from cryptography.hazmat.primitives.asymmetric import rsa
from io import BytesIO

def generate_rsa_signature_keys(bit_length=2048):
    """Membuat kunci RSA Signature dalam bentuk angka besar."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bit_length
    )
    public_key = private_key.public_key()

    # Mengambil angka besar dari kunci
    n = private_key.private_numbers().public_numbers.n  # Modulus
    e = private_key.private_numbers().public_numbers.e  # Eksponen publik
    d = private_key.private_numbers().d  # Eksponen privat

    return n, e, d

def save_keys_as_txt(n, e, d):
    """Menyimpan kunci ke file TXT untuk diunduh."""
    output = f"n (Modulus): {n}\n\n"
    output += f"e (Eksponen Publik): {e}\n\n"
    output += f"d (Eksponen Privat): {d}\n"

    # Simpan ke BytesIO untuk diunduh
    file = BytesIO()
    file.write(output.encode())
    file.seek(0)
    return file
