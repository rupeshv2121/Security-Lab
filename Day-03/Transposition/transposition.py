# ============================================
#          SIMPLE TRANSPOSITION CIPHER
# ============================================


def encrypt(text, columns):

    rows = (len(text) + columns - 1) // columns

    matrix = []

    index = 0

    for i in range(rows):

        row = []

        for j in range(columns):

            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append("")

        matrix.append(row)

    ciphertext = ""

    for col in range(columns):

        for row in range(rows):

            if matrix[row][col] != "":
                ciphertext += matrix[row][col]

    return ciphertext


def decrypt(ciphertext, columns):

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
print("      SIMPLE TRANSPOSITION")
print("================================")

plaintext = input("Enter plaintext: ")

columns = int(input("Enter number of columns: "))

ciphertext = encrypt(plaintext, columns)

print("\nCiphertext:")
print(ciphertext)

decrypted = decrypt(ciphertext, columns)

print("\nDecrypted Text:")
print(decrypted)