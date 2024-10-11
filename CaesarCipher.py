# Caesar Cipher Encryption and Decryption

# Function to encrypt using Caesar Cipher
def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            char = char.upper()  # Convert all characters to uppercase
            shift = ord('A')  # Use uppercase letters for shifting
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)  # Shift character
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext

# Function to decrypt using Caesar Cipher
def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabetic characters
            shift = ord('A')  # Use uppercase letters for shifting
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)  # Reverse shift
            plaintext += decrypted_char
        else:
            plaintext += char  # Non-alphabet characters remain unchanged
    return plaintext

# Example Usage
key = 3  # Shift key
message = "nishatmahmud"

print("Original Message:", message)
ciphertext = caesar_encrypt(message, key)
print("Encrypted Message:", ciphertext)
decrypted_message = caesar_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)