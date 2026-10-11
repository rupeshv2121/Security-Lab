# ============================================
#        CIRCULAR CHARACTER SHIFT
# ============================================


def left_shift(text, shift):

    if len(text) == 0:
        return text

    shift = shift % len(text)

    return text[shift:] + text[:shift]


def right_shift(text, shift):

    if len(text) == 0:
        return text

    shift = shift % len(text)

    return text[-shift:] + text[:-shift]


# ================= MAIN =================

print("================================")
print("       CIRCULAR SHIFT")
print("================================")

plaintext = input("Enter text: ")

shift = int(
    input("Enter shift value: ")
)


ciphertext = left_shift(
    plaintext,
    shift
)

print("\nEncrypted:")
print(ciphertext)


decrypted = right_shift(
    ciphertext,
    shift
)

print("\nDecrypted:")
print(decrypted)