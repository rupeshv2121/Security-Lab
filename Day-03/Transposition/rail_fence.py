# ============================================
#             RAIL FENCE CIPHER
# ============================================


def encrypt(text, rails):

    if rails <= 1:
        return text

    fence = []

    for i in range(rails):
        fence.append("")

    row = 0
    direction = 1

    for ch in text:

        fence[row] += ch

        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row += direction

    ciphertext = ""

    for i in range(rails):
        ciphertext += fence[i]

    return ciphertext


def decrypt(ciphertext, rails):

    if rails <= 1:
        return ciphertext

    pattern = []

    row = 0
    direction = 1

    for i in range(len(ciphertext)):

        pattern.append(row)

        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row += direction

    count = []

    for i in range(rails):
        count.append(0)

    for r in pattern:
        count[r] += 1

    fence = []

    index = 0

    for i in range(rails):

        rail = []

        for j in range(count[i]):

            rail.append(ciphertext[index])
            index += 1

        fence.append(rail)

    position = []

    for i in range(rails):
        position.append(0)

    plaintext = ""

    for r in pattern:

        plaintext += fence[r][position[r]]

        position[r] += 1

    return plaintext


# ================= MAIN =================

print("================================")
print("       RAIL FENCE CIPHER")
print("================================")

plaintext = input("Enter plaintext: ")

rails = int(input("Enter number of rails: "))

ciphertext = encrypt(plaintext, rails)

print("\nEncrypted Text:")
print(ciphertext)

decrypted = decrypt(ciphertext, rails)

print("\nDecrypted Text:")
print(decrypted)