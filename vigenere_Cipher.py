#vigenere cipher
#this repeat the key values for encrypted 
text , key = "SAJAND","SD"

key = (key*(len(text)//len(key)+1))[:len(text)]

#this key repeat SD upto length of sajan

encrypt = "".join([chr((ord(t)+ord(k) -2*65)%26+65) for t,k in zip(text,key)])
print(encrypt)

decrypt = "".join([chr((ord(e) - ord(k) -2*65)%26+65) for e,k in zip(encrypt,key)])
print(decrypt)
