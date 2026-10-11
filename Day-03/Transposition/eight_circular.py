# ============================================
#          8-BIT CIRCULAR ROTATION
# ============================================


def rotate_left(value, bits):

    bits = bits % 8

    result = (
        (value << bits)
        |
        (value >> (8 - bits))
    )

    return result & 255


def rotate_right(value, bits):

    bits = bits % 8

    result = (
        (value >> bits)
        |
        (value << (8 - bits))
    )

    return result & 255


def to_hex(data):

    digits = "0123456789ABCDEF"

    result = ""

    for value in data:

        result += digits[value // 16]
        result += digits[value % 16]

    return result


def from_hex(text):

    digits = "0123456789ABCDEF"

    data = []

    i = 0

    while i < len(text):

        high = 0
        low = 0

        for j in range(16):

            if digits[j] == text[i]:
                high = j

            if digits[j] == text[i + 1]:
                low = j

        data.append(
            high * 16 + low
        )

        i += 2

    return data


# ================= MAIN =================

print("================================")
print("        8-BIT ROTATION")
print("================================")

plaintext = input("Enter plaintext: ")

bits = int(
    input("Enter rotation (1-7): ")
)


if bits < 1 or bits > 7:

    print("Rotation must be between 1 and 7.")

else:

    encrypted = []

    for ch in plaintext:

        encrypted.append(
            rotate_left(
                ord(ch),
                bits
            )
        )

    ciphertext = to_hex(
        encrypted
    )

    print("\nCiphertext (Hex):")
    print(ciphertext)


    data = from_hex(
        ciphertext
    )

    decrypted = ""

    for value in data:

        decrypted += chr(
            rotate_right(
                value,
                bits
            )
        )

    print("\nDecrypted Text:")
    print(decrypted)