def vernam_cipher(text, key):
    result = ""
    for i in range(len(text)):
        ch_val = ord(text[i]) ^ ord(key[i % len(key)])
        result += chr(ch_val)
    return result

plainText = input("Enter the Plaintext : ")
key = input("Enter the Key : ")

encrypted_text = vernam_cipher(plainText, key)
print("Encrypted Text : ", encrypted_text)

decrypted_text = vernam_cipher(encrypted_text, key)
print("Decrypted Text : ", decrypted_text)






print("===== VERNAM CIPHER =====")

text = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted = ""
decrypted = ""

range_size = 95


# Check key length

if len(text) != len(key):

    print("Error: Key length must be equal to plaintext length.")

else:

    # ---------------- ENCRYPTION ----------------

    for i in range(len(text)):

        P = ord(text[i]) - 32
        K = ord(key[i]) - 32

        C = (P + K) % range_size

        encrypted += chr(C + 32)


    # ---------------- DECRYPTION ----------------

    for i in range(len(encrypted)):

        C = ord(encrypted[i]) - 32
        K = ord(key[i]) - 32

        P = (C - K + range_size) % range_size

        decrypted += chr(P + 32)


    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)