# Vigenère Cipher Encryption and Decryption

# Function to generate the key in a repeated manner to match the length of the message
def generate_key(plaintext, key):
    key = key.upper()
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# Function to encrypt using Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    key = generate_key(plaintext, key)
    
    ciphertext = ""
    for i in range(len(plaintext)):
        # Shift the character based on the key
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        encrypted_char = chr((p + k) % 26 + ord('A'))
        ciphertext += encrypted_char
    
    return ciphertext

# Function to decrypt using Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    
    plaintext = ""
    for i in range(len(ciphertext)):
        # Reverse the shift based on the key
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        decrypted_char = chr((c - k + 26) % 26 + ord('A'))  # +26 ensures we avoid negative mod
        plaintext += decrypted_char
    
    return plaintext

# Example Usage
message = "nishatmahmud"
key = "KEYWORD"

print("Original Message:", message)
ciphertext = vigenere_encrypt(message, key)
print("Encrypted Message:", ciphertext)
decrypted_message = vigenere_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)