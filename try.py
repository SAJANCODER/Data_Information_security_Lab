#caesar cipher

text = "sajan".upper()
key = 4
encrypted = "".join([chr((ord(x)-65+key)%26+65) for x in text])
print(f"encrypted text :{encrypted}")
decrypted  = "".join([chr((ord(z)-65-key)%26+65)for z in encrypted])
print(f"decrypted text:{decrypted}")


#vigenier cipher

text = "sajan".upper()
key = "SD"

key = (key * (len(text)//len(key)+1))[:len(text)]
encrypted = "".join([chr((ord(t)+ord(k) -2*65)%26+65) for t,k in zip(text,key)])
print(encrypted)

decrypted = "".join([chr((ord(e)-ord(k) -2*65)%26+65) for e, k in zip(encrypted,key)])
print(decrypted)

#playfair cipher
from pycipher import Playfair
pf = Playfai("KEYWORDS")
enc = pf.encipher("HELXLO")
dec = pf.decipher(encv)
print(dec)
