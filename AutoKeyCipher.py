# Auto Key Cipher Encryption and Decryption

# Function to generate the key for Auto Key Cipher
def generate_auto_key(plaintext, key):
    key = key.upper()
    key = list(key)
    # Append the plaintext itself to the key after the keyword
    key.extend(list(plaintext)[:len(plaintext) - len(key)])
    return "".join(key)

# Function to encrypt using Auto Key Cipher
def auto_key_encrypt(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    key = generate_auto_key(plaintext, key)
    
    ciphertext = ""
    for i in range(len(plaintext)):
        # Shift the character based on the key
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        encrypted_char = chr((p + k) % 26 + ord('A'))
        ciphertext += encrypted_char
    
    return ciphertext

# Function to decrypt using Auto Key Cipher
def auto_key_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ""
    
    for i in range(len(ciphertext)):
        # Reverse the shift based on the key
        c = ord(ciphertext[i]) - ord('A')
        if i < len(key):
            k = ord(key[i]) - ord('A')
        else:
            k = ord(plaintext[i - len(key)]) - ord('A')  # Use decrypted plaintext as part of the key
        decrypted_char = chr((c - k + 26) % 26 + ord('A'))  # +26 to avoid negative mod
        plaintext += decrypted_char
    
    return plaintext

# Example Usage
message = "nishatmahmud"
key = "KEYWORD"

print("Original Message:", message)
ciphertext = auto_key_encrypt(message, key)
print("Encrypted Message:", ciphertext)
decrypted_message = auto_key_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)