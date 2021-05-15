# Quick-RSA
A concise implementation of a textbook version [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). Supports encryption and decryption of an english sentence.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Quick-RSA.

```bash
pip install quickrsa
```

## Usage
```python
max_len = 128
public_key, private_key = generate.generate_keys(max_len)

message = 'HELLO WORLD'
encrypted_message = encdec.encrypt(public_key, message, max_len)
decrypted_message = encdec.decrypt(encrypted_message, private_key, public_key)
```

Example code in run.py
```bash
usage: run.py [-h] [-l MAX_LEN] [-m MESSAGE]

optional arguments:
  -l MAX_LEN, --max-len MAX_LEN
                        maximum message length
  -m MESSAGE, --message MESSAGE
                        message to encrypt
```