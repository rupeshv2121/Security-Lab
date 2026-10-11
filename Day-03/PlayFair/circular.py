def create_matrix(key):
    # Printable ASCII characters: 32 to 126
    characters = ""

    for i in range(32, 127):
        characters += chr(i)

    used = ""

    # Put unique key characters first
    for ch in key:
        if ch in characters and ch not in used:
            used += ch

    # Add remaining characters
    for ch in characters:
        if ch not in used:
            used += ch

    # Create 10 x 10 matrix
    matrix = []

    for i in range(10):
        row = []

        for j in range(10):
            index = i * 10 + j

            if index < len(used):
                row.append(used[index])
            else:
                row.append('\0')

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    print("\n========== PLAYFAIR MATRIX ==========")

    for i in range(10):
        for j in range(10):

            ch = matrix[i][j]

            if ch == ' ':
                print("[SP]", end=" ")
            elif ch == '\0':
                print("[  ]", end=" ")
            else:
                print("[" + ch + "]", end=" ")

        print()

    print("======================================")


def find_position(matrix, ch):

    for i in range(10):
        for j in range(10):

            if matrix[i][j] == ch:
                return i, j

    return -1, -1


def get_filler(ch):

    if ch != 'X':
        return 'X'

    if ch != 'Q':
        return 'Q'

    return '#'


def prepare_text(text):

    pairs = []

    i = 0

    while i < len(text):

        # If only one character is left
        if i == len(text) - 1:

            filler = get_filler(text[i])

            pairs.append(text[i] + filler)

            i += 1

        # If both characters are same
        elif text[i] == text[i + 1]:

            filler = get_filler(text[i])

            pairs.append(text[i] + filler)

            i += 1

        # Normal pair
        else:

            pairs.append(text[i] + text[i + 1])

            i += 2

    return pairs


def encrypt(pairs, matrix):

    ciphertext = ""

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:

            ciphertext += matrix[r1][(c1 + 1) % 10]
            ciphertext += matrix[r2][(c2 + 1) % 10]

        # Same column
        elif c1 == c2:

            ciphertext += matrix[(r1 + 1) % 10][c1]
            ciphertext += matrix[(r2 + 1) % 10][c2]

        # Rectangle rule
        else:

            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]

    return ciphertext


def decrypt(ciphertext, matrix):

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        a = ciphertext[i]
        b = ciphertext[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:

            plaintext += matrix[r1][(c1 - 1) % 10]
            plaintext += matrix[r2][(c2 - 1) % 10]

        # Same column
        elif c1 == c2:

            plaintext += matrix[(r1 - 1) % 10][c1]
            plaintext += matrix[(r2 - 1) % 10][c2]

        # Rectangle rule
        else:

            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


def circular_left_shift(text, shift):

    n = len(text)

    if n == 0:
        return text

    shift = shift % n

    return text[shift:] + text[:shift]


def circular_right_shift(text, shift):

    n = len(text)

    if n == 0:
        return text

    shift = shift % n

    return text[-shift:] + text[:-shift]


# =========================================
#              MAIN PROGRAM
# =========================================

print("==========================================")
print("       EXTENDED PLAYFAIR CIPHER")
print("==========================================")

key = input("Enter the key: ")
plaintext = input("Enter plaintext: ")

# Create Playfair matrix
matrix = create_matrix(key)

# Display matrix
display_matrix(matrix)


# -----------------------------------------
# PREPARE PLAINTEXT
# -----------------------------------------

pairs = prepare_text(plaintext)

print("\nPrepared Plaintext:")

for pair in pairs:
    print(pair, end=" ")

print()


# -----------------------------------------
# PLAYFAIR ENCRYPTION
# -----------------------------------------

playfair_ciphertext = encrypt(pairs, matrix)

print("\nPlayfair Ciphertext:")
print(playfair_ciphertext)


# -----------------------------------------
# CIRCULAR SHIFT
# -----------------------------------------

shift = int(input("\nEnter circular left shift value: "))

final_ciphertext = circular_left_shift(
    playfair_ciphertext,
    shift
)

print("\nFinal Ciphertext after Circular Shift:")
print(final_ciphertext)


# =========================================
#              DECRYPTION
# =========================================

print("\n==========================================")
print("              DECRYPTION")
print("==========================================")


# Reverse circular shift
original_ciphertext = circular_right_shift(
    final_ciphertext,
    shift
)

print("\nAfter Reverse Circular Shift:")
print(original_ciphertext)


# Playfair decryption
decrypted_text = decrypt(
    original_ciphertext,
    matrix
)

print("\nDecrypted Text:")
print(decrypted_text)

print("\n==========================================")