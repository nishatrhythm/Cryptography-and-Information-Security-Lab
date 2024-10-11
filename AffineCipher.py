# Affine Cipher Encryption and Decryption

# Function to find the modular inverse of 'a' under modulo 'm'
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to encrypt using Affine Cipher
def affine_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            x = ord(char.upper()) - ord('A')  # Convert letter to number (A=0, B=1, ..., Z=25)
            encrypted_char = (a * x + b) % 26  # Apply Affine formula
            ciphertext += chr(encrypted_char + ord('A'))  # Convert number back to letter
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext

# Function to decrypt using Affine Cipher
def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = mod_inverse(a, 26)  # Find the modular inverse of 'a'
    if a_inv is None:
        return "Decryption not possible, 'a' has no modular inverse!"

    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabetic characters
            x = ord(char.upper()) - ord('A')  # Convert letter to number (A=0, B=1, ..., Z=25)
            decrypted_char = (a_inv * (x - b)) % 26  # Apply Affine decryption formula
            plaintext += chr(decrypted_char + ord('A'))  # Convert number back to letter
        else:
            plaintext += char  # Non-alphabet characters remain unchanged
    return plaintext

# Example Usage
key_a = 5  # Key 'a' (must be coprime with 26)
key_b = 8  # Key 'b'
message = "nishatmahmud"

print("Original Message:", message)
ciphertext = affine_encrypt(message, key_a, key_b)
print("Encrypted Message:", ciphertext)
decrypted_message = affine_decrypt(ciphertext, key_a, key_b)
print("Decrypted Message:", decrypted_message)