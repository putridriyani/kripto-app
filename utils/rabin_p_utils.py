from Crypto.Util import number

def generate_rabin_keys_as_numbers(key_size=2048):
    """Membuat pasangan kunci Rabin-P dalam bentuk angka besar."""
    p = number.getPrime(key_size // 2)
    q = number.getPrime(key_size // 2)
    n = p * q  # Modulus

    return p, q, n
