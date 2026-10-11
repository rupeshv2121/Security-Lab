# Decimal → Binary (8-bit)
def dec_to_bin(n):
    bits = []
    for i in range(8):
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))

# Binary → Decimal
def bin_to_dec(b):
    val = 0
    for bit in b:
        val = val * 2 + (1 if bit == '1' else 0)
    return val

# Decimal → Hex (2-digit)
def dec_to_hex(n):
    digits = "0123456789abcdef"
    return digits[n // 16] + digits[n % 16]

# Hex → Decimal
def hex_to_dec(h):
    digits = "0123456789abcdef"
    val = 0
    for ch in h:
        val = val * 16 + digits.index(ch.lower())
    return val









def vigenere_cipher(text, key, mode="enc", output="hex"):
    result = []
    for i, ch in enumerate(text):
        p = ord(ch)
        k = ord(key[i % len(key)])
        if mode == "enc":
            val = (p + k) % 256
        else:
            val = (p - k) % 256
        result.append(dec_to_bin(val) if output=="bin" else dec_to_hex(val))
    return " ".join(result)




def vernam_cipher(text, key, output="hex"):
    result = []
    for i, ch in enumerate(text):
        val = ord(ch) ^ ord(key[i % len(key)])
        result.append(dec_to_bin(val) if output=="bin" else dec_to_hex(val))
    return " ".join(result)




def gronsfeld_cipher(text, key, mode="enc", output="hex"):
    result = []
    for i, ch in enumerate(text):
        p = ord(ch)
        k = int(key[i % len(key)])
        if mode == "enc":
            val = (p + k) % 256
        else:
            val = (p - k) % 256
        result.append(dec_to_bin(val) if output=="bin" else dec_to_hex(val))
    return " ".join(result)



def beaufort_cipher(text, key, output="hex"):
    result = []
    for i, ch in enumerate(text):
        p = ord(ch)
        k = ord(key[i % len(key)])
        val = (k - p) % 256
        result.append(dec_to_bin(val) if output=="bin" else dec_to_hex(val))
    return " ".join(result)



plainText = "HELLO123!"
key = "KEY"

print("Vigenere Enc (hex):", vigenere_cipher(plainText, key, "enc", "hex"))
print("Vigenere Dec (bin):", vigenere_cipher(plainText, key, "dec", "bin"))

print("Vernam (bin):", vernam_cipher(plainText, key, "bin"))

print("Gronsfeld Enc (hex):", gronsfeld_cipher(plainText, "314159", "enc", "hex"))
print("Gronsfeld Dec (bin):", gronsfeld_cipher(plainText, "314159", "dec", "bin"))

print("Beaufort (hex):", beaufort_cipher(plainText, key, "hex"))
