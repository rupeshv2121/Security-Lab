def dec_to_bin(n):
    bits = []
    for i in range(8):
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))

def bin_to_dec(b):
    val = 0
    for bit in b:
        val = val * 2 + (1 if bit == '1' else 0)
    return val

def rotate(bin_str, r=2, direction="right"):
    r = r % len(bin_str)
    if direction == "right":
        return bin_str[-r:] + bin_str[:-r]
    else:
        return bin_str[r:] + bin_str[:r]

def vernam_encrypt(plainText, key):
    encrypted_text = ""
    cipher_bin = []
    for i in range(len(plainText)):
        c_val = ord(plainText[i]) ^ ord(key[i]) 
        encrypted_text += chr((c_val % 95) + 32)
        bin_val = dec_to_bin(c_val)
        rotated = rotate(bin_val, 2, "right")
        cipher_bin.append(rotated)
    return encrypted_text, cipher_bin

def vernam_decrypt(cipher_bin, key):
    key = (key * ((len(cipher_bin) // len(key)) + 1))[:len(cipher_bin)]
    plainText = ""
    for i in range(len(cipher_bin)):
        bin_val = rotate(cipher_bin[i], 2, "left")   
        c_val = bin_to_dec(bin_val)
        p_val = c_val ^ ord(key[i])                  
        plainText += chr(p_val)
    return plainText

print("===== VERNAM CIPHER =====")

plainText = input("Enter the Plaintext : ")
key = input("Enter the Key : ")
key = (key * ((len(plainText) // len(key)) + 1))[:len(plainText)]

encrypted_text, cipher_bin = "", []

choice = input("Enter your choice (1 for encryption, 2 for decryption, -1 to exit): ")
while choice != "-1":
    if choice == "1":
        encrypted_text, cipher_bin = vernam_encrypt(plainText, key)
        print("======================================")
        print("Encrypted Text :", encrypted_text)
        print("Ciphertext (binary rotated):", " ".join(cipher_bin))
        print("======================================")
    elif choice == "2":
        if cipher_bin:
            decrypted_text = vernam_decrypt(cipher_bin, key)
            print("---------------------------------------")
            print("Decrypted Text:", decrypted_text)
            print("---------------------------------------")
        else:
            print("No ciphertext available. Please encrypt first.")
    else:
        print("Invalid choice. Please try again.")
    choice = input("Enter your choice (1 for encryption, 2 for decryption, -1 to exit): ")
