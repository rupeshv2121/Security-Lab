# ============================================
#             SCYTALE CIPHER
# ============================================


def encrypt(text, columns):

    if columns <= 1:
        return text

    ciphertext = ""

    for col in range(columns):

        index = col

        while index < len(text):

            ciphertext += text[index]

            index += columns

    return ciphertext


def decrypt(ciphertext, columns):

    if columns <= 1:
        return ciphertext

    length = len(ciphertext)

    rows = (length + columns - 1) // columns

    matrix = []

    for i in range(rows):

        row = []

        for j in range(columns):
            row.append("")

        matrix.append(row)

    index = 0

    for col in range(columns):

        for row in range(rows):

            position = row * columns + col

            if position < length:

                matrix[row][col] = ciphertext[index]

                index += 1

    plaintext = ""

    for row in range(rows):

        for col in range(columns):

            if matrix[row][col] != "":
                plaintext += matrix[row][col]

    return plaintext


# ================= MAIN =================

print("================================")
print("          SCYTALE CIPHER")
print("================================")

plaintext = input("Enter plaintext: ")

columns = int(
    input("Enter number of columns: ")
)

ciphertext = encrypt(
    plaintext,
    columns
)

print("\nCiphertext:")
print(ciphertext)

decrypted = decrypt(
    ciphertext,
    columns
)

print("\nDecrypted Text:")
print(decrypted)