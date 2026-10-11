# ============================================
#     PLAYFAIR + KEY DEPENDENT SHIFT
#                 VERSION 4
# ============================================


# --------------------------------------------
# GET CHARACTER SET
# --------------------------------------------

def get_characters(size):

    if size == 5:

        return "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    elif size == 6:

        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    elif size == 8:

        return (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789"
            "!@"
        )

    elif size == 10:

        characters = ""

        for i in range(32, 127):

            characters += chr(i)

        return characters

    return ""


# --------------------------------------------
# CREATE PLAYFAIR MATRIX
# --------------------------------------------

def create_matrix(key, size):

    characters = get_characters(size)

    used = ""

    # Classical 5 x 5
    if size == 5:

        key = key.upper()
        key = key.replace('J', 'I')

    # Add key characters
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
# FIND POSITION
# --------------------------------------------

def find_position(matrix, size, ch):

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

    # 5 x 5
    if size == 5:

        text = text.upper()

        for ch in text:

            if ch >= 'A' and ch <= 'Z':

                if ch == 'J':

                    ch = 'I'

                clean_text += ch

    # Extended matrices
    else:

        for ch in text:

            if ch in characters:

                clean_text += ch

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
# PLAYFAIR ENCRYPTION
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
# PLAYFAIR DECRYPTION
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


# --------------------------------------------
# CALCULATE KEY-DEPENDENT SHIFT
# --------------------------------------------

def calculate_key_shift(key, length):

    if length == 0:

        return 0

    total = 0

    for ch in key:

        total += ord(ch)

    shift = total % length

    return shift


# --------------------------------------------
# CIRCULAR LEFT SHIFT
# --------------------------------------------

def circular_left_shift(text, shift):

    if len(text) == 0:

        return text

    shift = shift % len(text)

    return text[shift:] + text[:shift]


# --------------------------------------------
# CIRCULAR RIGHT SHIFT
# --------------------------------------------

def circular_right_shift(text, shift):

    if len(text) == 0:

        return text

    shift = shift % len(text)

    if shift == 0:

        return text

    return text[-shift:] + text[:-shift]


# ============================================
#                 MAIN PROGRAM
# ============================================

print("============================================")
print("   PLAYFAIR + KEY DEPENDENT SHIFT")
print("============================================")


# --------------------------------------------
# INPUT
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

filler = input(
    "\nEnter filler character: "
)


if len(filler) != 1:

    print("Filler must be one character.")
    exit()


if filler not in characters:

    print(
        "Filler is not available "
        "in the selected matrix."
    )

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
# PLAYFAIR ENCRYPTION
# --------------------------------------------

ciphertext = encrypt(
    pairs,
    matrix,
    size
)


print("\nPlayfair Ciphertext:")
print(ciphertext)


# ============================================
# KEY DEPENDENT SHIFT
# ============================================

shift = calculate_key_shift(
    key,
    len(ciphertext)
)


print("\nKey-dependent shift value:")
print(shift)


# --------------------------------------------
# APPLY CIRCULAR LEFT SHIFT
# --------------------------------------------

ciphertext = circular_left_shift(
    ciphertext,
    shift
)


print("\nAfter Key-dependent Circular Shift:")
print(ciphertext)


# ============================================
# FINAL CIPHERTEXT
# ============================================

print("\n============================================")
print("             FINAL CIPHERTEXT")
print("============================================")

print(ciphertext)


# ============================================
#                 DECRYPTION
# ============================================

print("\n============================================")
print("                  DECRYPTION")
print("============================================")


# --------------------------------------------
# REVERSE CIRCULAR SHIFT
# --------------------------------------------

ciphertext = circular_right_shift(
    ciphertext,
    shift
)


print("\nAfter Reverse Circular Shift:")
print(ciphertext)


# --------------------------------------------
# PLAYFAIR DECRYPTION
# --------------------------------------------

decrypted_text = decrypt(
    ciphertext,
    matrix,
    size
)


print("\nDecrypted Text:")
print(decrypted_text)


print("\n============================================")
print("                    END")
print("============================================")