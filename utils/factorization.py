import time

def factorize(n: int):
    """Melakukan faktorisasi brute force terhadap n."""
    start_time = time.time()
    factors = []
    
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)

    execution_time = time.time() - start_time
    return factors, execution_time
