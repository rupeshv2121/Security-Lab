def gronsfeld_enc_cipher(text, key):
    result = ""
    for i, ch in enumerate(text):
        p = ord(ch) - 32  # shift into printable ASCII range
        k = int(key[i % len(key)])  # numeric key digit
        ch_val = (p + k) % 95       # wrap around printable range
        result += chr(ch_val + 32)
    return result

def gronsfeld_dec_cipher(text, key):
    result = ""
    for i, ch in enumerate(text):
        p = ord(ch) - 32
        k = int(key[i % len(key)])
        ch_val = (p - k) % 95
        result += chr(ch_val + 32)
    return result

plainText = input("Enter the Plaintext : ")
key = input("Enter the Numeric Key (digits only): ")

encrypted_text = gronsfeld_enc_cipher(plainText, key)
print("Encrypted Text : ", encrypted_text)

decrypted_text = gronsfeld_dec_cipher(encrypted_text, key)
print("Decrypted Text : ", decrypted_text)
