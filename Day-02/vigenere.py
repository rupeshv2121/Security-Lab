def vigenere_enc_cipher(text, key):
    result = ""
    key_index = 0
    for ch in text:
        if ch.isalpha():
            p = ord(ch.upper()) - ord('A')
            k = ord(key[key_index % len(key)].upper()) - ord('A')
            ch_val = (p + k) % 26
          
            if ch.isupper():
                result += chr(ch_val + ord('A'))
            else:
                result += chr(ch_val + ord('a'))
            key_index += 1
        else:
            result += ch  
    return result

def vigenere_dec_cipher(text, key):
    result = ""
    key_index = 0
    for ch in text:
        if ch.isalpha(): 
            p = ord(ch.upper()) - ord('A')
            k = ord(key[key_index % len(key)].upper()) - ord('A')
            ch_val = (p - k) % 26

            if ch.isupper():
                result += chr(ch_val + ord('A'))
            else:
                result += chr(ch_val + ord('a'))
            key_index += 1
        else:
            result += ch  
    return result

plainText = input("Enter the Plaintext : ")
key = input("Enter the Key : ")

encrypted_text = vigenere_enc_cipher(plainText, key)
print("Encrypted Text : ", encrypted_text)

decrypted_text = vigenere_dec_cipher(encrypted_text, key)
print("Decrypted Text : ", decrypted_text)


def vigenere_enc_cipher(text, key):
    result = ""
    key_index = 0
    for ch in text:
        p = ord(ch) - 32  # shift into printable ASCII range
        k = ord(key[key_index % len(key)]) - 32
        ch_val = (p + k) % 95  # 95 printable characters
        result += chr(ch_val + 32)
        key_index += 1
    return result

def vigenere_dec_cipher(text, key):
    result = ""
    key_index = 0
    for ch in text:
        p = ord(ch) - 32
        k = ord(key[key_index % len(key)]) - 32
        ch_val = (p - k) % 95
        result += chr(ch_val + 32)
        key_index += 1
    return result

plainText = input("Enter the Plaintext : ")
key = input("Enter the Key : ")

encrypted_text = vigenere_enc_cipher(plainText, key)
print("Encrypted Text : ", encrypted_text)

decrypted_text = vigenere_dec_cipher(encrypted_text, key)
print("Decrypted Text : ", decrypted_text)




















alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("===== VIGENERE CIPHER =====")

text = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted = ""
decrypted = ""

# Convert text and key to uppercase manually
new_text = ""
for ch in text:
    if ch >= 'a' and ch <= 'z':
        ch = alphabet[ord(ch) - ord('a')]
    new_text += ch

text = new_text

new_key = ""
for ch in key:
    if ch >= 'a' and ch <= 'z':
        ch = alphabet[ord(ch) - ord('a')]
    new_key += ch

key = new_key


# Encryption
key_index = 0

for ch in text:

    if ch >= 'A' and ch <= 'Z':

        P = alphabet.index(ch)
        K = alphabet.index(key[key_index])

        C = (P + K) % 26

        encrypted += alphabet[C]

        key_index += 1

        if key_index == len(key):
            key_index = 0

    else:
        encrypted += ch


# Decryption
key_index = 0

for ch in encrypted:

    if ch >= 'A' and ch <= 'Z':

        C = alphabet.index(ch)
        K = alphabet.index(key[key_index])

        P = (C - K + 26) % 26

        decrypted += alphabet[P]

        key_index += 1

        if key_index == len(key):
            key_index = 0

    else:
        decrypted += ch


print("\nEncrypted Text:", encrypted)
print("Decrypted Text:", decrypted)












print("===== VIGENERE CIPHER =====")

text = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted = ""
decrypted = ""

key_index = 0

# ASCII printable characters: 32 to 126
range_size = 95


# ---------------- ENCRYPTION ----------------

for ch in text:

    P = ord(ch) - 32
    K = ord(key[key_index]) - 32

    C = (P + K) % range_size

    encrypted += chr(C + 32)

    key_index += 1

    if key_index == len(key):
        key_index = 0


# ---------------- DECRYPTION ----------------

key_index = 0

for ch in encrypted:

    C = ord(ch) - 32
    K = ord(key[key_index]) - 32

    P = (C - K + range_size) % range_size

    decrypted += chr(P + 32)

    key_index += 1

    if key_index == len(key):
        key_index = 0


print("\nEncrypted Text:", encrypted)
print("Decrypted Text:", decrypted)














# -------------------------------
# Manual Conversion Functions
# -------------------------------

# Decimal → Binary (8-bit)
def dec_to_bin(n):
    bits = []
    for i in range(8):
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))

# Binary → Decimal
def bin_to_dec(b):
    val = 0
    for bit in b:
        val = val * 2 + (1 if bit == '1' else 0)
    return val

# Decimal → Hex (2-digit)
def dec_to_hex(n):
    digits = "0123456789abcdef"
    return digits[n // 16] + digits[n % 16]

# Hex → Decimal
def hex_to_dec(h):
    digits = "0123456789abcdef"
    val = 0
    for ch in h:
        val = val * 16 + digits.index(ch.lower())
    return val

# -------------------------------
# Vigenère Cipher (Printable ASCII 32–126)
# -------------------------------

def vigenere_cipher(text, key, mode="enc", output="hex"):
    result = []
    for i, ch in enumerate(text):
        p = ord(ch) - 32          # shift into printable range
        k = ord(key[i % len(key)]) - 32
        if mode == "enc":
            val = (p + k) % 95    # wrap around 95 printable chars
        else:
            val = (p - k) % 95
        final_val = val + 32      # shift back into printable ASCII
        result.append(dec_to_bin(final_val) if output=="bin" else dec_to_hex(final_val))
    return " ".join(result)

# -------------------------------
# Example Run
# -------------------------------

plainText = "Hello, World! 123 @#$"
key = "KEY"

print("Plaintext:", plainText)

# Encrypt in hex
encrypted_hex = vigenere_cipher(plainText, key, "enc", "hex")
print("Encrypted (hex):", encrypted_hex)

# Encrypt in binary
encrypted_bin = vigenere_cipher(plainText, key, "enc", "bin")
print("Encrypted (bin):", encrypted_bin)

# Decrypt back (hex output just for inspection)
decrypted_hex = vigenere_cipher(plainText, key, "dec", "hex")
print("Decrypted (hex):", decrypted_hex)
