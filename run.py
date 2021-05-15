from argparse import ArgumentParser
from quickrsa import generate, encdec

parser = ArgumentParser()
parser.add_argument('-l', '--max-len', type=int, default=128, help='maximum message length')
parser.add_argument('-m', '--message', type=str, default='HELLO WORLD', help='message to encrypt')
args = parser.parse_args()

max_len = args.max_len
public_key, private_key = generate.generate_keys(max_len)

message = args.message.upper()
encrypted_message = encdec.encrypt(public_key, message, max_len)
decrypted_message = encdec.decrypt(encrypted_message, private_key, public_key)

print(f'Message to encrypt: {message}')
print(f'Encrypted message: {encrypted_message}')
print(f'Decrypted message: {decrypted_message}')