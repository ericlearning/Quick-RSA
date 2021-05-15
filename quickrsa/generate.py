import random
from .euclidean import extended_ea
from .prime import is_prime_miller_rabin, totient_for_prime_product

def generate_p_and_q(N):
	primes = []
	while True:
		candidate = random.randint(5, 10**(N//2))
		is_prime = is_prime_miller_rabin(candidate, 10)
		if is_prime:
			primes.append(candidate)
		if len(primes) >= 2:
			break
	return primes

def generate_e(phi):
	while True:
		candidate = random.randint(2, phi)
		gcd, s, _ = extended_ea(candidate, phi)

		if gcd == 1:
			return candidate, s

def generate_keys(max_len=128):
    p, q = generate_p_and_q(max_len)
    n = p * q
    phi = totient_for_prime_product(p, q)
    e, d = generate_e(phi)
    return (e, n), d