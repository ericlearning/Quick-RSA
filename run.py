from textbook_rsa import generate, encdec

max_len = 128
public_key, private_key = generate.generate_keys(max_len)

message = "HELLO WORLD".upper()
encrypted_message = encdec.encrypt(public_key, message, max_len)
decrypted_message = encdec.decrypt(encrypted_message, private_key, public_key)

print(message)
print(encrypted_message)
print(decrypted_message)