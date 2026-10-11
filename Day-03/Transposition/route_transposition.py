# ============================================
#          ROUTE TRANSPOSITION
# ============================================


def encrypt(text, rows, columns):

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

    # Read columns top to bottom

    for col in range(columns):

        for row in range(rows):

            if matrix[row][col] != "":

                ciphertext += matrix[row][col]

    return ciphertext


def decrypt(ciphertext, rows, columns):

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

            if position < len(ciphertext):

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
print("        ROUTE TRANSPOSITION")
print("================================")

plaintext = input("Enter plaintext: ")

rows = int(input("Enter number of rows: "))

columns = int(
    input("Enter number of columns: ")
)


ciphertext = encrypt(
    plaintext,
    rows,
    columns
)

print("\nCiphertext:")
print(ciphertext)


decrypted = decrypt(
    ciphertext,
    rows,
    columns
)

print("\nDecrypted Text:")
print(decrypted)