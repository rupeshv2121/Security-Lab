# ============================================
#             ASCII SHIFT CIPHER
# ============================================


def encrypt(text, shift):

    result = ""

    for ch in text:

        value = ord(ch)

        value = (
            (value - 32 + shift) % 95
        ) + 32

        result += chr(value)

    return result


def decrypt(text, shift):

    result = ""

    for ch in text:

        value = ord(ch)

        value = (
            (value - 32 - shift) % 95
        ) + 32

        result += chr(value)

    return result


# ================= MAIN =================

print("================================")
print("          ASCII SHIFT")
print("================================")

plaintext = input("Enter plaintext: ")

shift = int(
    input("Enter shift value: ")
)


ciphertext = encrypt(
    plaintext,
    shift
)

print("\nCiphertext:")
print(ciphertext)


decrypted = decrypt(
    ciphertext,
    shift
)

print("\nDecrypted Text:")
print(decrypted)