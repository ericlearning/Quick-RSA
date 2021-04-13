import math
import random

def extended_ea(r1, r2, s1=1, s2=0, t1=0, t2=1):
	if r2 == 0:
		if s1 < 0:
			s1 += s2
		if t1 < 0:
			t1 += t2
		return r1, s1, t1
	q, r = r1//r2, r1%r2
	s, t = s1-s2*q, t1-t2*q
	return extended_ea(r2, r, s2, s, t2, t)

def ea(r1, r2):
	if r2 == 0:
		return r1
	r = r1%r2
	return ea(r2, r)

def fast_modular_exponent(base, exp, mod):
	y = 1
	bin_exp = bin(exp)[-1:1:-1]
	for cur_bin in bin_exp:
		if int(cur_bin):
			y = (base * y) % mod
		base = (base ** 2) % mod
	return y

def is_prime_miller_rabin(n, k):
	assert n > 3
	if n%2 == 0:
		return 0

	r = 0
	n_test = n-1
	while True:
		if n_test%2 == 0:
			n_test //= 2
			r += 1
		else:
			d = n_test
			break

	for _ in range(k):
		is_continue = False
		a = random.randint(2, n-2)
		x = fast_modular_exponent(a, d, n)

		if x == 1 or x == n-1:
			continue

		for _ in range(r-1):
			x = (x ** 2) % n
			if x == n-1:
				is_continue = True
				break

		if is_continue:
			continue
		return 0
	return 1

def totient_for_prime_product(p, q):
	return (p-1) * (q-1)

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


max_len = 128
p, q = generate_p_and_q(max_len)
n = p * q
phi = totient_for_prime_product(p, q)
e, d = generate_e(phi)
print(f"[Bob] Public Key: e={e} | n={n}")


MSG = "HELLO WORLD"
assert len(MSG) < max_len//2
assert MSG.isupper()
M = int(''.join([str(ord(ch)) for ch in MSG]))
C = fast_modular_exponent(M, e, n)
print(f"[Alice] Message Sent: C={C}")


N = str(fast_modular_exponent(C, d, n))
if len(N) % 2 == 1:
	N = '0' + N
N = ''.join([chr(int(N[i*2] + N[i*2+1])) for i in range(len(N)//2)])
print(f"[Bob] Message Received: N={N}")