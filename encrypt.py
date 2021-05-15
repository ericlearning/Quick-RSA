generate_public_key(max_len)


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