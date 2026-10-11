# ============================================
#       EXTENDED PLAYFAIR CIPHER
#             VERSION 6
#
# Features:
# 1. User-selectable matrix
# 2. User-selectable filler
# 3. Multiple Playfair rounds
# 4. Key-dependent circular shift
# 5. Reverse ciphertext
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

    # For classical 5 x 5 Playfair
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

    print("\n================ PLAYFAIR MATRIX ================")

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

    print("==================================================")


# --------------------------------------------
# FIND CHARACTER POSITION
# --------------------------------------------

def find_position(matrix, size, ch):

    # J is treated as I in 5 x 5
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
    # 5 x 5
    # ----------------------------------------

    if size == 5:

        text = text.upper()

        for ch in text:

            if ch >= 'A' and ch <= 'Z':

                if ch == 'J':

                    ch = 'I'

                clean_text += ch

    # ----------------------------------------
    # EXTENDED MATRICES
    # ----------------------------------------

    else:

        for ch in text:

            if ch in characters:

                clean_text += ch

    # ----------------------------------------
    # CREATE DIGRAPHS
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
# PLAYFAIR ENCRYPTION
# --------------------------------------------

def playfair_encrypt(text, matrix, size):

    ciphertext = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

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

def playfair_decrypt(text, matrix, size):

    plaintext = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

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
# KEY-DEPENDENT SHIFT
# --------------------------------------------

def calculate_key_shift(key, length):

    if length == 0:

        return 0

    total = 0

    for ch in key:

        total += ord(ch)

    return total % length


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
#                  MAIN
# ============================================

print("================================================")
print("          EXTENDED PLAYFAIR CIPHER")
print("================================================")


# --------------------------------------------
# INPUT
# --------------------------------------------

key = input("Enter Playfair key: ")

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
        "Filler is not present "
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

display_matrix(
    matrix,
    size
)


# --------------------------------------------
# PREPARE PLAINTEXT ONCE
# --------------------------------------------

pairs = prepare_text(
    plaintext,
    filler,
    size
)

prepared_text = ""

for pair in pairs:

    prepared_text += pair


print("\nPrepared Plaintext:")
print(prepared_text)


# ============================================
# NUMBER OF PLAYFAIR ROUNDS
# ============================================

rounds = int(
    input(
        "\nEnter number of Playfair rounds: "
    )
)

if rounds < 1:

    rounds = 1


# ============================================
# MULTIPLE PLAYFAIR ENCRYPTION
# ============================================

ciphertext = prepared_text


for i in range(rounds):

    ciphertext = playfair_encrypt(
        ciphertext,
        matrix,
        size
    )

    print(
        "\nAfter Playfair Round",
        i + 1,
        ":"
    )

    print(ciphertext)


# ============================================
# KEY-DEPENDENT CIRCULAR SHIFT
# ============================================

shift = calculate_key_shift(
    key,
    len(ciphertext)
)

print("\nKey-dependent shift value:")
print(shift)


ciphertext = circular_left_shift(
    ciphertext,
    shift
)

print("\nAfter Circular Shift:")
print(ciphertext)


# ============================================
# REVERSE CIPHERTEXT
# ============================================

ciphertext = ciphertext[::-1]

print("\nAfter Reversing Ciphertext:")
print(ciphertext)


# ============================================
# FINAL CIPHERTEXT
# ============================================

print("\n================================================")
print("               FINAL CIPHERTEXT")
print("================================================")

print(ciphertext)


# ============================================
#                  DECRYPTION
# ============================================

print("\n================================================")
print("                  DECRYPTION")
print("================================================")


# --------------------------------------------
# UNDO REVERSAL
# --------------------------------------------

ciphertext = ciphertext[::-1]

print("\nAfter Undoing Reversal:")
print(ciphertext)


# --------------------------------------------
# UNDO CIRCULAR SHIFT
# --------------------------------------------

ciphertext = circular_right_shift(
    ciphertext,
    shift
)

print("\nAfter Undoing Circular Shift:")
print(ciphertext)


# --------------------------------------------
# MULTIPLE PLAYFAIR DECRYPTION
# --------------------------------------------

decrypted_text = ciphertext


for i in range(rounds):

    decrypted_text = playfair_decrypt(
        decrypted_text,
        matrix,
        size
    )

    print(
        "\nAfter Playfair Decryption Round",
        rounds - i,
        ":"
    )

    print(decrypted_text)


# ============================================
# FINAL PLAINTEXT
# ============================================

print("\n================================================")
print("                FINAL PLAINTEXT")
print("================================================")

print(decrypted_text)


print("\n================================================")
print("                    END")
print("================================================")