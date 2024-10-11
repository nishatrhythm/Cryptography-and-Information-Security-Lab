# Keyless Transposition Cipher Encryption and Decryption

# Function to encrypt using Keyless Transposition Cipher
def transposition_encrypt(plaintext):
    # Remove spaces from the plaintext and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    
    # Calculate the number of columns (can use square root or fixed size)
    length = len(plaintext)
    columns = int(length ** 0.5)  # Use square root for determining grid size
    if columns * columns < length:
        columns += 1  # Adjust number of columns if necessary
    
    # Create a grid (list of rows)
    grid = [plaintext[i:i+columns] for i in range(0, len(plaintext), columns)]
    
    # Read characters column by column to form ciphertext
    ciphertext = ""
    for col in range(columns):
        for row in grid:
            if col < len(row):  # Avoid index error for uneven rows
                ciphertext += row[col]
    
    return ciphertext

# Function to decrypt using Keyless Transposition Cipher
def transposition_decrypt(ciphertext):
    # Calculate the number of columns (same logic as encryption)
    length = len(ciphertext)
    columns = int(length ** 0.5)
    if columns * columns < length:
        columns += 1  # Adjust number of columns if necessary
    
    # Calculate number of rows
    rows = (length + columns - 1) // columns  # Ceiling division to determine rows
    
    # Recreate the grid column by column
    grid = [''] * rows
    col_length = length // rows + 1 if length % rows else length // rows
    
    idx = 0
    for col in range(columns):
        for row in range(rows):
            if idx < length and len(grid[row]) < col_length:
                grid[row] += ciphertext[idx]
                idx += 1
    
    # Read row by row to get the plaintext
    plaintext = ''.join(grid)
    
    return plaintext

# Example Usage
message = "nishatmahmud"
print("Original Message:", message)
ciphertext = transposition_encrypt(message)
print("Encrypted Message:", ciphertext)
decrypted_message = transposition_decrypt(ciphertext)
print("Decrypted Message:", decrypted_message)