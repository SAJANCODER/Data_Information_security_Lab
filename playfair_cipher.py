from pycipher import Playfair

# Key and Plaintext
key = "AUGUST"
text = "HACKATHONATRIT".replace("J", "I")

# Add padding 'X' if length is odd
if len(text) % 2 != 0:
    text += "X"

pf = Playfair(key)
encrypted = pf.encipher(text)
decrypted = pf.decipher(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
