#implement of caesar cipher

text = input("enter the text you want to encrypt:")
text=text.upper()
#on behalf of using caesar cipher we need to use key for swap
#Plain:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Key=3:   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

key = 7
encrypt = "".join([chr((ord(x)-65+key)%26+65) for x in text])
print(f"Encrypted Text:{encrypt}")

decrypt = "".join([chr((ord(z)-65-key)%26+65) for z in encrypt])

authentication = input("If u want to see the decrypted text (y/n):")
authentication = authentication.lower()
if (authentication == 'y'):
    print(f"Decrypted Text:{decrypt}")
else:
    exit()
