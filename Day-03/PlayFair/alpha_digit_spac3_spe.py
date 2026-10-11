# ============================================
#        EXTENDED PLAYFAIR CIPHER
#              VERSION 2
# ============================================


# --------------------------------------------
# GET CHARACTER SET
# --------------------------------------------

def get_characters(size):

    if size == 5:

        # Classical Playfair
        # I and J are combined
        return "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    elif size == 6:

        # A-Z + 0-9
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    elif size == 8:

        # A-Z + a-z + 0-9 + 2 symbols
        return (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789"
            "!@"
        )

    elif size == 10:

        # Printable ASCII characters
        characters = ""

        for i in range(32, 127):
            characters += chr(i)

        return characters

    return ""


# --------------------------------------------
# CREATE MATRIX
# --------------------------------------------

def create_matrix(key, size):

    characters = get_characters(size)

    used = ""

    # For 5 x 5 Playfair
    if size == 5:

        key = key.upper()
        key = key.replace('J', 'I')

    # Add unique characters from key
    for ch in key:

        if ch in characters and ch not in used:

            used += ch

    # Add remaining characters
    for ch in characters:

        if ch not in used:

            used += ch

    matrix = []

    for i in range(size):

        row = []

        for j in range(size):

            index = i * size + j

            if index < len(used):

                row.append(used[index])

            else:

                row.append('\0')

        matrix.append(row)

    return matrix


# --------------------------------------------
# DISPLAY MATRIX
# --------------------------------------------

def display_matrix(matrix, size):

    print("\nPlayfair Matrix:")
    print("----------------")

    for i in range(size):

        for j in range(size):

            ch = matrix[i][j]

            if ch == ' ':

                print("[SP]", end=" ")

            elif ch == '\0':

                print("[ ]", end=" ")

            else:

                print("[" + ch + "]", end=" ")

        print()


# --------------------------------------------
# FIND CHARACTER POSITION
# --------------------------------------------

def find_position(matrix, size, ch):

    # J is treated as I in 5x5
    if size == 5 and ch == 'J':

        ch = 'I'

    for i in range(size):

        for j in range(size):

            if matrix[i][j] == ch:

                return i, j

    return -1, -1


# --------------------------------------------
# PREPARE PLAINTEXT
# --------------------------------------------

def prepare_text(text, filler, size):

    characters = get_characters(size)

    clean_text = ""

    # ----------------------------------------
    # 5 x 5 CASE
    # ----------------------------------------

    if size == 5:

        text = text.upper()

        for ch in text:

            if ch >= 'A' and ch <= 'Z':

                if ch == 'J':

                    ch = 'I'

                clean_text += ch

    # ----------------------------------------
    # EXTENDED CASES
    # ----------------------------------------

    else:

        for ch in text:

            if ch in characters:

                clean_text += ch

    # ----------------------------------------
    # CREATE PAIRS
    # ----------------------------------------

    pairs = []

    i = 0

    while i < len(clean_text):

        # Last character
        if i == len(clean_text) - 1:

            pairs.append(
                clean_text[i] + filler
            )

            i += 1

        # Repeated characters
        elif clean_text[i] == clean_text[i + 1]:

            pairs.append(
                clean_text[i] + filler
            )

            i += 1

        # Normal pair
        else:

            pairs.append(
                clean_text[i] +
                clean_text[i + 1]
            )

            i += 2

    return pairs


# --------------------------------------------
# ENCRYPTION
# --------------------------------------------

def encrypt(pairs, matrix, size):

    ciphertext = ""

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        r1, c1 = find_position(
            matrix,
            size,
            a
        )

        r2, c2 = find_position(
            matrix,
            size,
            b
        )

        # Same row
        if r1 == r2:

            ciphertext += matrix[r1][
                (c1 + 1) % size
            ]

            ciphertext += matrix[r2][
                (c2 + 1) % size
            ]

        # Same column
        elif c1 == c2:

            ciphertext += matrix[
                (r1 + 1) % size
            ][c1]

            ciphertext += matrix[
                (r2 + 1) % size
            ][c2]

        # Rectangle
        else:

            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]

    return ciphertext


# --------------------------------------------
# DECRYPTION
# --------------------------------------------

def decrypt(ciphertext, matrix, size):

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        a = ciphertext[i]
        b = ciphertext[i + 1]

        r1, c1 = find_position(
            matrix,
            size,
            a
        )

        r2, c2 = find_position(
            matrix,
            size,
            b
        )

        # Same row
        if r1 == r2:

            plaintext += matrix[r1][
                (c1 - 1) % size
            ]

            plaintext += matrix[r2][
                (c2 - 1) % size
            ]

        # Same column
        elif c1 == c2:

            plaintext += matrix[
                (r1 - 1) % size
            ][c1]

            plaintext += matrix[
                (r2 - 1) % size
            ][c2]

        # Rectangle
        else:

            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


# ============================================
#                 MAIN
# ============================================

print("============================================")
print("       EXTENDED PLAYFAIR CIPHER")
print("============================================")


# --------------------------------------------
# INPUT KEY AND PLAINTEXT
# --------------------------------------------

key = input("Enter key: ")

plaintext = input("Enter plaintext: ")


# --------------------------------------------
# MATRIX SIZE
# --------------------------------------------

print("\nSelect Matrix Size:")

print("1. 5 x 5  -> A-Z")
print("2. 6 x 6  -> A-Z + 0-9")
print("3. 8 x 8  -> A-Z + a-z + 0-9 + symbols")
print("4. 10 x 10 -> Printable ASCII")


choice = input("Enter choice: ")


if choice == '1':

    size = 5

elif choice == '2':

    size = 6

elif choice == '3':

    size = 8

elif choice == '4':

    size = 10

else:

    print("Invalid choice.")
    exit()


# --------------------------------------------
# FILLER CHARACTER
# --------------------------------------------

characters = get_characters(size)

print("\nChoose a filler character.")

filler = input("Enter filler: ")


if len(filler) != 1:

    print("Filler must be exactly one character.")
    exit()


if filler not in characters:

    print("Filler is not present in this matrix.")
    exit()


# --------------------------------------------
# CREATE MATRIX
# --------------------------------------------

matrix = create_matrix(
    key,
    size
)


# --------------------------------------------
# DISPLAY MATRIX
# --------------------------------------------

display_matrix(
    matrix,
    size
)


# --------------------------------------------
# PREPARE PLAINTEXT
# --------------------------------------------

pairs = prepare_text(
    plaintext,
    filler,
    size
)


print("\nPrepared Plaintext:")

for pair in pairs:

    print(pair, end=" ")

print()


# --------------------------------------------
# ENCRYPT
# --------------------------------------------

ciphertext = encrypt(
    pairs,
    matrix,
    size
)


print("\nEncrypted Text:")
print(ciphertext)


# --------------------------------------------
# DECRYPT
# --------------------------------------------

decrypted_text = decrypt(
    ciphertext,
    matrix,
    size
)


print("\nDecrypted Text:")
print(decrypted_text)


print("\n============================================")
print("                  END")
print("============================================")