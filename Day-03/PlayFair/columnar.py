# ============================================
#       EXTENDED PLAYFAIR CIPHER
#             VERSION 7
#
# Features:
# 1. User-selectable matrix
# 2. User-selectable filler
# 3. Multiple Playfair rounds
# 4. Key-dependent circular shift
# 5. Reverse ciphertext
# 6. Columnar Transposition
# ============================================


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


def create_matrix(key, size):

    characters = get_characters(size)

    used = ""

    if size == 5:
        key = key.upper()
        key = key.replace('J', 'I')

    for ch in key:

        if ch in characters and ch not in used:
            used += ch

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


def find_position(matrix, size, ch):

    if size == 5 and ch == 'J':
        ch = 'I'

    for i in range(size):

        for j in range(size):

            if matrix[i][j] == ch:
                return i, j

    return -1, -1


def prepare_text(text, filler, size):

    characters = get_characters(size)

    clean_text = ""

    if size == 5:

        text = text.upper()

        for ch in text:

            if ch >= 'A' and ch <= 'Z':

                if ch == 'J':
                    ch = 'I'

                clean_text += ch

    else:

        for ch in text:

            if ch in characters:
                clean_text += ch

    pairs = []

    i = 0

    while i < len(clean_text):

        if i == len(clean_text) - 1:

            pairs.append(clean_text[i] + filler)

            i += 1

        elif clean_text[i] == clean_text[i + 1]:

            pairs.append(clean_text[i] + filler)

            i += 1

        else:

            pairs.append(clean_text[i] + clean_text[i + 1])

            i += 2

    return pairs


def playfair_encrypt(text, matrix, size):

    ciphertext = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, size, a)
        r2, c2 = find_position(matrix, size, b)

        # Same row
        if r1 == r2:

            ciphertext += matrix[r1][(c1 + 1) % size]
            ciphertext += matrix[r2][(c2 + 1) % size]

        # Same column
        elif c1 == c2:

            ciphertext += matrix[(r1 + 1) % size][c1]
            ciphertext += matrix[(r2 + 1) % size][c2]

        # Rectangle rule
        else:

            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]

    return ciphertext


def playfair_decrypt(text, matrix, size):

    plaintext = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, size, a)
        r2, c2 = find_position(matrix, size, b)

        # Same row
        if r1 == r2:

            plaintext += matrix[r1][(c1 - 1) % size]
            plaintext += matrix[r2][(c2 - 1) % size]

        # Same column
        elif c1 == c2:

            plaintext += matrix[(r1 - 1) % size][c1]
            plaintext += matrix[(r2 - 1) % size][c2]

        # Rectangle rule
        else:

            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


def calculate_key_shift(key, length):

    if length == 0:
        return 0

    total = 0

    for ch in key:
        total += ord(ch)

    return total % length


def circular_left_shift(text, shift):

    if len(text) == 0:
        return text

    shift = shift % len(text)

    return text[shift:] + text[:shift]


def circular_right_shift(text, shift):

    if len(text) == 0:
        return text

    shift = shift % len(text)

    if shift == 0:
        return text

    return text[-shift:] + text[:-shift]


# ==========================================================
#           COLUMNAR TRANSPOSITION
# ==========================================================


def get_column_order(key):

    # Store (character, original position)
    columns = []

    for i in range(len(key)):
        columns.append((key[i], i))

    # Sort alphabetically.
    # Original position handles duplicate characters.
    columns.sort()

    order = []

    for item in columns:
        order.append(item[1])

    return order


def columnar_encrypt(text, key):

    if len(key) == 0:
        return text

    columns = len(key)

    # Create rows
    rows = []

    i = 0

    while i < len(text):

        row = []

        for j in range(columns):

            if i < len(text):
                row.append(text[i])
                i += 1

            else:
                break

        rows.append(row)

    order = get_column_order(key)

    ciphertext = ""

    # Read columns according to alphabetical key order
    for col in order:

        for row in rows:

            if col < len(row):
                ciphertext += row[col]

    return ciphertext


def columnar_decrypt(text, key):

    if len(key) == 0:
        return text

    columns = len(key)
    length = len(text)

    rows_count = (length + columns - 1) // columns

    # Number of characters in each column
    column_lengths = []

    for col in range(columns):

        if col < length % columns:
            column_lengths.append(rows_count)

        elif length % columns == 0:
            column_lengths.append(rows_count)

        else:
            column_lengths.append(rows_count - 1)

    order = get_column_order(key)

    # Store characters column-wise
    matrix = []

    for i in range(columns):
        matrix.append([])

    index = 0

    for col in order:

        count = column_lengths[col]

        for j in range(count):

            matrix[col].append(text[index])

            index += 1

    # Read matrix row-wise
    plaintext = ""

    for row in range(rows_count):

        for col in range(columns):

            if row < len(matrix[col]):
                plaintext += matrix[col][row]

    return plaintext


# ==========================================================
#                    MAIN PROGRAM
# ==========================================================


print("================================================")
print("          EXTENDED PLAYFAIR CIPHER")
print("                 VERSION 7")
print("================================================")


key = input("Enter Playfair key: ")

plaintext = input("Enter plaintext: ")


# ----------------------------------------------------------
# MATRIX SIZE
# ----------------------------------------------------------

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


characters = get_characters(size)


# ----------------------------------------------------------
# FILLER
# ----------------------------------------------------------

filler = input("\nEnter filler character: ")


if len(filler) != 1:

    print("Filler must be one character.")
    exit()


if filler not in characters:

    print("Filler is not present in the selected matrix.")
    exit()


# ----------------------------------------------------------
# CREATE MATRIX
# ----------------------------------------------------------

matrix = create_matrix(key, size)

display_matrix(matrix, size)


# ----------------------------------------------------------
# PREPARE PLAINTEXT
# ----------------------------------------------------------

pairs = prepare_text(plaintext, filler, size)

prepared_text = ""

for pair in pairs:
    prepared_text += pair


print("\nPrepared Plaintext:")
print(prepared_text)


# ----------------------------------------------------------
# MULTIPLE PLAYFAIR ROUNDS
# ----------------------------------------------------------

rounds = int(input("\nEnter number of Playfair rounds: "))


if rounds < 1:
    rounds = 1


ciphertext = prepared_text


for i in range(rounds):

    ciphertext = playfair_encrypt(
        ciphertext,
        matrix,
        size
    )

    print("\nAfter Playfair Round", i + 1, ":")
    print(ciphertext)


# ----------------------------------------------------------
# KEY-DEPENDENT CIRCULAR SHIFT
# ----------------------------------------------------------

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


# ----------------------------------------------------------
# REVERSE
# ----------------------------------------------------------

ciphertext = ciphertext[::-1]


print("\nAfter Reversing Ciphertext:")
print(ciphertext)


# ----------------------------------------------------------
# COLUMNAR TRANSPOSITION
# ----------------------------------------------------------

print("\nColumnar Transposition Key:")
print(key)


ciphertext = columnar_encrypt(
    ciphertext,
    key
)


print("\nAfter Columnar Transposition:")
print(ciphertext)


# ----------------------------------------------------------
# FINAL CIPHERTEXT
# ----------------------------------------------------------

print("\n================================================")
print("               FINAL CIPHERTEXT")
print("================================================")

print(ciphertext)


# ==========================================================
#                     DECRYPTION
# ==========================================================


print("\n================================================")
print("                  DECRYPTION")
print("================================================")


# ----------------------------------------------------------
# UNDO COLUMNAR TRANSPOSITION
# ----------------------------------------------------------

ciphertext = columnar_decrypt(
    ciphertext,
    key
)


print("\nAfter Undoing Columnar Transposition:")
print(ciphertext)


# ----------------------------------------------------------
# UNDO REVERSE
# ----------------------------------------------------------

ciphertext = ciphertext[::-1]


print("\nAfter Undoing Reversal:")
print(ciphertext)


# ----------------------------------------------------------
# UNDO CIRCULAR SHIFT
# ----------------------------------------------------------

ciphertext = circular_right_shift(
    ciphertext,
    shift
)


print("\nAfter Undoing Circular Shift:")
print(ciphertext)


# ----------------------------------------------------------
# PLAYFAIR DECRYPTION
# ----------------------------------------------------------

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


# ----------------------------------------------------------
# FINAL PLAINTEXT
# ----------------------------------------------------------

print("\n================================================")
print("                FINAL PLAINTEXT")
print("================================================")

print(decrypted_text)


print("\n================================================")
print("                    END")
print("================================================")