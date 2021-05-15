from .prime import fast_modular_exponent

def encrypt(public_key, message, max_len):
    e, n = public_key
    assert len(message) < max_len//2
    assert message.isupper()
    M = int(''.join([str(ord(ch)) for ch in message]))
    C = fast_modular_exponent(M, e, n)
    return C

def decrypt(encrypted_message, private_key, public_key):
    e, n = public_key
    N = str(fast_modular_exponent(encrypted_message, private_key, n))
    if len(N) % 2 == 1:
        N = '0' + N
    N = ''.join([chr(int(N[i*2] + N[i*2+1])) for i in range(len(N)//2)])
    return N