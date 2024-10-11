# Multiplicative Cipher Encryption and Decryption

# Function to find the modular inverse of 'a' under modulo 'm'
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to encrypt using Multiplicative Cipher
def multiplicative_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            char = char.upper()  # Convert to uppercase
            x = ord(char) - ord('A')  # Convert letter to number (A=0, B=1, ..., Z=25)
            encrypted_char = (key * x) % 26  # Apply multiplicative cipher formula
            ciphertext += chr(encrypted_char + ord('A'))  # Convert number back to letter
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext

# Function to decrypt using Multiplicative Cipher
def multiplicative_decrypt(ciphertext, key):
    plaintext = ""
    a_inv = mod_inverse(key, 26)  # Find the modular inverse of 'a'
    if a_inv is None:
        return "Decryption not possible, 'a' has no modular inverse!"

    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabetic characters
            x = ord(char) - ord('A')  # Convert letter to number (A=0, B=1, ..., Z=25)
            decrypted_char = (a_inv * x) % 26  # Apply decryption formula
            plaintext += chr(decrypted_char + ord('A'))  # Convert number back to letter
        else:
            plaintext += char  # Non-alphabet characters remain unchanged
    return plaintext

# Example Usage
key = 5  # Key 'a' (must be coprime with 26)
message = "nishatmahmud"

print("Original Message:", message)
ciphertext = multiplicative_encrypt(message, key)
print("Encrypted Message:", ciphertext)
decrypted_message = multiplicative_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)