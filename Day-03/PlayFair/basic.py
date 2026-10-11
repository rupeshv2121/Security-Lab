# ============================================
#          BASIC PLAYFAIR CIPHER
# ============================================

def create_matrix(key):

    key = key.upper()
    key = key.replace('J', ' I')

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    used = ""

    for ch in key:
        if ch >= 'A' and ch <= 'Z':
            if ch not in used:
                used += ch

    for ch in alphabet:
        if ch not in used:
            used += ch

    matrix = []

    for i in range(5):
        row = []
        for j in range(5):
            row.append(used[i * 5 + j])
        matrix.append(row)

    return matrix


def display_matrix(matrix):

    print("\nPlayfair Matrix:")
    print("----------------")

    for i in range(5):
        for j in range(5):
            print(matrix[i][j], end=" ")
        print()


def find_position(matrix, ch):

    if ch == 'J':
        ch = 'I'

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

    return -1, -1


def prepare_text(text):

    text = text.upper()

    clean_text = ""

    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            if ch == 'J':
                ch = 'I'
            clean_text += ch

    pairs = []
    i = 0

    while i < len(clean_text):
        if i == len(clean_text) - 1:
            pairs.append(clean_text[i] + 'X')
            i += 1

        elif clean_text[i] == clean_text[i + 1]:
            pairs.append(clean_text[i] + 'X')
            i += 1

        else:
            pairs.append(
                clean_text[i] + clean_text[i + 1]
            )
            i += 2

    return pairs


def encrypt(pairs, matrix):

    ciphertext = ""
    for pair in pairs:
        a = pair[0]
        b = pair[1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5]
            ciphertext += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1]
            ciphertext += matrix[(r2 + 1) % 5][c2]

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

        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]

        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


print("==========================================")
print("          BASIC PLAYFAIR CIPHER")
print("==========================================")

key = input("Enter key: ")
plaintext = input("Enter plaintext: ")


matrix = create_matrix(key)
display_matrix(matrix)

pairs = prepare_text(plaintext)
print("\nPrepared Plaintext:")

for pair in pairs:
    print(pair, end=" ")

print()

ciphertext = encrypt(pairs, matrix)
print("\n\nCiphertext:")
print(ciphertext)


decrypted_text = decrypt(ciphertext, matrix)
print("\nDecrypted Text:")
print(decrypted_text)


print("\n==========================================")