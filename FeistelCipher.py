# Feistel Cipher Encryption and Decryption

# Example round function (could be more complex in real ciphers)
def round_function(right, subkey):
    return right ^ subkey  # XOR right half with the subkey

# Function to perform Feistel Cipher encryption
def feistel_encrypt(plaintext, subkeys, num_rounds=4):
    # Split plaintext into left and right halves
    left = plaintext >> 16  # Upper 16 bits as left half
    right = plaintext & 0xFFFF  # Lower 16 bits as right half
    
    # Perform the Feistel rounds
    for i in range(num_rounds):
        temp = right
        right = left ^ round_function(right, subkeys[i])  # Apply round function and XOR with left half
        left = temp  # Swap halves
    
    # Combine the final left and right halves
    ciphertext = (left << 16) | right
    return ciphertext

# Function to perform Feistel Cipher decryption
def feistel_decrypt(ciphertext, subkeys, num_rounds=4):
    # Split ciphertext into left and right halves
    left = ciphertext >> 16  # Upper 16 bits as left half
    right = ciphertext & 0xFFFF  # Lower 16 bits as right half
    
    # Perform the Feistel rounds in reverse order
    for i in range(num_rounds - 1, -1, -1):
        temp = left
        left = right ^ round_function(left, subkeys[i])  # Apply round function and XOR with right half
        right = temp  # Swap halves
    
    # Combine the final left and right halves
    plaintext = (left << 16) | right
    return plaintext

# Example Usage
# Subkeys for each round (in real ciphers, these would be derived from a master key)
subkeys = [0x1234, 0x5678, 0x9ABC, 0xDEF0]

# Plaintext and Ciphertext are 32-bit integers (split into two 16-bit halves)
plaintext = 0xABCD1234  # Example plaintext
print(f"Original Plaintext: {hex(plaintext).upper()}")

# Encrypt the plaintext
ciphertext = feistel_encrypt(plaintext, subkeys)
print(f"Encrypted Ciphertext: {hex(ciphertext).upper()}")

# Decrypt the ciphertext
decrypted_plaintext = feistel_decrypt(ciphertext, subkeys)
print(f"Decrypted Plaintext: {hex(decrypted_plaintext).upper()}")