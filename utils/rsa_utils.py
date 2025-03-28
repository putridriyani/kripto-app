from cryptography.hazmat.primitives.asymmetric import rsa

def generate_rsa_keys_as_numbers(key_size=2048):
    """Membuat pasangan kunci RSA dalam bentuk angka besar."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )
    public_key = private_key.public_key()

    # Konversi ke angka besar
    n = private_key.private_numbers().public_numbers.n  # Modulus
    e = private_key.private_numbers().public_numbers.e  # Eksponen publik
    d = private_key.private_numbers().d  # Eksponen privat

    return n, e, d
