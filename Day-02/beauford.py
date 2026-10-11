def beaufort_cipher(text, key):
    result = ""
    for i, ch in enumerate(text.upper()):
        if ch.isalpha():
            p = ord(ch) - ord('A')
            k = ord(key[i % len(key)].upper()) - ord('A')
            ch_val = (k - p) % 26
            result += chr(ch_val + ord('A'))
        else:
            result += ch
    return result

plainText = input("Enter the Plaintext : ")
key = input("Enter the Key : ")

encrypted_text = beaufort_cipher(plainText, key)
print("Encrypted Text : ", encrypted_text)

decrypted_text = beaufort_cipher(encrypted_text, key)  # same function
print("Decrypted Text : ", decrypted_text)
