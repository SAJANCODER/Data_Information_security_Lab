#fernet is a part of cryptography library
from cryptography.fernet import Fernet

#generate a key to encrypt and decrypt (bcz fernet use same key for both)
key = Fernet.generate_key()
cipher = Fernet(key)

sensitive_data = input(b"enter the sensitive data :")
encrpt = cipher.encrypt(sensitive_data)
print(encrypt)