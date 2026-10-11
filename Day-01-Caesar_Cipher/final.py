def caesar_cipher(text, key):
    result = ""

    for ch in text:
        symbol = ord(ch)

        # Uppercase letters
        if symbol >= 65 and symbol <= 90:
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))

        # Lowercase letters
        elif symbol >= 97 and symbol <= 122:
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

        # Numbers
        elif symbol >= 48 and symbol <= 57:
            result += chr((ord(ch) - ord('0') + key) % 10 + ord('0'))

        # Space
        elif symbol == 32:
            result += chr((ord(ch) - ord(' ') + key) % 1 + ord(' '))

        # Special characters: ! to /
        elif symbol >= 33 and symbol <= 47:
            result += chr((ord(ch) - ord('!') + key) % 15 + ord('!'))

        # Special characters: : to @
        elif symbol >= 58 and symbol <= 64:
            result += chr((ord(ch) - ord(':') + key) % 7 + ord(':'))

        # Special characters: [ to `
        elif symbol >= 91 and symbol <= 96:
            result += chr((ord(ch) - ord('[') + key) % 6 + ord('['))

        # Special characters: { to ~
        elif symbol >= 123 and symbol <= 126:
            result += chr((ord(ch) - ord('{') + key) % 4 + ord('{'))

    return result


def banner():
    print("==============================================")
    print("              CAESAR CIPHER")
    print("==============================================")
    print("        Encryption / Decryption Tool")
    print("==============================================")


def main():

    while True:
        banner()

        print("\nSelect an option:")
        print()
        print("  [1] Caesar Cipher")
        print("  [2] Len Algorithm")
        print("  [3] Exit")
        print()

        ask = input("Enter your choice: ").strip()

        # Exit
        if ask == '3':
            print("\nExiting program...")
            print("Thank you for using Caesar Cipher!")
            break

        # Invalid choice
        if ask != '1' and ask != '2':
            print("\nWrong Input!!")
            input("\nPress Enter to continue...")
            continue

        print("\n----------------------------------------------")

        text = input("Enter the PlainText: ")

        if len(text) == 0:
            print("\nPlainText cannot be empty!")
            input("\nPress Enter to continue...")
            continue

        inpLen = len(text)

        print("----------------------------------------------")
        print("PlainText Length :", inpLen)

        # Caesar Cipher
        if ask == '1':
            key = 3

            print("Algorithm        : Caesar Cipher")
            print("Key              :", key)

            encrypted_text = caesar_cipher(text, key)
            print("\nEncryption : ", encrypted_text)

            decrypted_text = caesar_cipher(encrypted_text, -key)
            print("Decryption : ", decrypted_text)

        # Len Algorithm
        elif ask == '2':
            key = inpLen

            print("Algorithm        : Len Algorithm")
            print("Key              :", key)

            encrypted_text = caesar_cipher(text, key)
            print("\nEncryption : ", encrypted_text)

            decrypted_text = caesar_cipher(encrypted_text, -key)
            print("Decryption : ", decrypted_text)

        print("----------------------------------------------")
        again = input("\nPress Enter to continue or type 'q' to quit: ")

        if again.lower() == 'q':
            print("\nExiting program...")
            break


if __name__ == "__main__":
    main()