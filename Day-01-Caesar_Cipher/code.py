def caesar_cipher(text, key):
    result = ""
    for ch in text:
        symbol = ord(ch)
        if symbol >= 65 and symbol <= 90:
            result +=  chr((ord(ch)-ord('A')+ key) % 26 + ord('A'))
        elif symbol >= 97 and symbol <= 122:
            result +=  chr((ord(ch)-ord('a')+ key) % 26 + ord('a'))
        elif symbol >= 48 and symbol <= 57:
            result +=  chr((ord(ch)-ord('0')+ key) % 10 + ord('0'))
        elif symbol == 32:
            result +=  chr((ord(ch)-ord(' ')+ key) % 1 + ord(' '))
        elif symbol >= 33 and symbol <= 47:
            result +=  chr((ord(ch)-ord('!')+ key) % 15 + ord('!'))
        elif symbol >= 58 and symbol <= 64:
            result +=  chr((ord(ch)-ord(':')+ key) % 7 + ord(':'))
        elif symbol >= 91 and symbol <= 96:
            result +=  chr((ord(ch)-ord('[')+ key) % 6 + ord('['))
        elif symbol >= 123 and symbol <= 126:
            result +=  chr((ord(ch)-ord('{')+ key) % 4 + ord('{'))

    return result

text = input("Enter the plainText: ")
inpLen = len(text)

ask = input("do you want Caesar_Cipher or Len ? Select (C/L)")

if(ask == 'C'):
    encrypted_text = caesar_cipher(text, 3)
    print("Encryption : ", encrypted_text)
    
    decrypted_text = caesar_cipher(encrypted_text, -3)
    print("Decryption : ", decrypted_text)
elif (ask == 'L') :
    print("Performing Len Algorithm and Plaintext Len = ", inpLen)
    encrypted_text = caesar_cipher(text, inpLen)
    print("Encryption : ", encrypted_text)
    
    decrypted_text = caesar_cipher(encrypted_text, -inpLen)
    print("Decryption : ", decrypted_text)
else:
    print("Wrong Input!!")

