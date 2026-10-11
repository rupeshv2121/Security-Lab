# ============================================
#       DOUBLE COLUMNAR TRANSPOSITION
# ============================================


def get_order(key):

    items = []

    for i in range(len(key)):
        items.append((key[i], i))

    items.sort()

    order = []

    for item in items:
        order.append(item[1])

    return order


def encrypt_columnar(text, key):

    columns = len(key)

    matrix = []

    index = 0

    while index < len(text):

        row = []

        for i in range(columns):

            if index < len(text):

                row.append(text[index])
                index += 1

        matrix.append(row)

    order = get_order(key)

    result = ""

    for col in order:

        for row in matrix:

            if col < len(row):
                result += row[col]

    return result


def decrypt_columnar(ciphertext, key):

    columns = len(key)

    length = len(ciphertext)

    rows = (length + columns - 1) // columns

    remainder = length % columns

    lengths = []

    for col in range(columns):

        if remainder == 0:
            lengths.append(rows)

        elif col < remainder:
            lengths.append(rows)

        else:
            lengths.append(rows - 1)

    matrix = []

    for i in range(columns):
        matrix.append([])

    order = get_order(key)

    index = 0

    for col in order:

        for i in range(lengths[col]):

            matrix[col].append(ciphertext[index])

            index += 1

    result = ""

    for row in range(rows):

        for col in range(columns):

            if row < len(matrix[col]):
                result += matrix[col][row]

    return result


# ================= MAIN =================

print("================================")
print("      DOUBLE COLUMNAR CIPHER")
print("================================")

plaintext = input("Enter plaintext: ")

key1 = input("Enter first key: ")
key2 = input("Enter second key: ")


ciphertext = encrypt_columnar(
    plaintext,
    key1
)

print("\nAfter First Transposition:")
print(ciphertext)


ciphertext = encrypt_columnar(
    ciphertext,
    key2
)

print("\nAfter Second Transposition:")
print(ciphertext)


decrypted = decrypt_columnar(
    ciphertext,
    key2
)

decrypted = decrypt_columnar(
    decrypted,
    key1
)

print("\nFinal Decrypted Text:")
print(decrypted)