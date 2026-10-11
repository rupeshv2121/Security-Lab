# ============================================
#          COLUMNAR TRANSPOSITION
#          Padded Version
# ============================================


def get_order(key):

    items = []

    # Store key character along with its original position
    for i in range(len(key)):
        items.append((key[i], i))

    # Sort alphabetically
    items.sort()

    order = []

    # Store original column positions
    for item in items:
        order.append(item[1])

    return order


# ============================================
#              ENCRYPTION
# ============================================

def encrypt(text, key):

    columns = len(key)

    # Padding
    while len(text) % columns != 0:
        text += 'X'

    matrix = []

    index = 0

    # Create matrix row by row
    while index < len(text):

        row = []

        for i in range(columns):

            row.append(text[index])
            index += 1

        matrix.append(row)

    # Get column reading order
    order = get_order(key)

    ciphertext = ""

    # Read columns according to key order
    for col in order:

        for row in matrix:

            ciphertext += row[col]

    return ciphertext


# ============================================
#              DECRYPTION
# ============================================

def decrypt(ciphertext, key):

    columns = len(key)

    rows = len(ciphertext) // columns

    matrix = []

    # Create empty columns
    for i in range(columns):
        matrix.append([])

    # Get column reading order
    order = get_order(key)

    index = 0

    # Fill columns according to key order
    for col in order:

        for i in range(rows):

            matrix[col].append(ciphertext[index])
            index += 1

    plaintext = ""

    # Read matrix row by row
    for row in range(rows):

        for col in range(columns):

            plaintext += matrix[col][row]

    return plaintext


# ============================================
#                  MAIN
# ============================================

print("================================")
print("      COLUMNAR TRANSPOSITION")
print("================================")

plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

# Convert key to uppercase
key = key.upper()

# Encrypt
ciphertext = encrypt(plaintext, key)

print("\nCiphertext:")
print(ciphertext)

# Decrypt
decrypted = decrypt(ciphertext, key)

print("\nDecrypted Text:")
print(decrypted)

# Remove padding for displaying original text
while len(decrypted) > 0 and decrypted[-1] == 'X':
    decrypted = decrypted[:-1]

print("\nOriginal Text:")
print(decrypted)