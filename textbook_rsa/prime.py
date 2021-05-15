import random

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