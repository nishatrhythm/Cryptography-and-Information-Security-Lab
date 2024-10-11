# Keyed Transposition Cipher Encryption and Decryption

# Function to get the order of columns based on the sorted key
def get_key_order(key):
    key = key.upper()
    sorted_key = sorted(list(key))
    key_order = []
    
    for char in key:
        index = sorted_key.index(char)
        key_order.append(index)
        sorted_key[index] = None  # Mark as used
    
    return key_order

# Function to encrypt using Keyed Transposition Cipher
def keyed_transposition_encrypt(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()  # Make sure the key is also in uppercase
    key_order = get_key_order(key)
    
    # Determine number of columns (equal to the length of the key)
    num_columns = len(key)
    num_rows = len(plaintext) // num_columns + (len(plaintext) % num_columns > 0)
    
    # Fill the grid row by row
    grid = [plaintext[i:i + num_columns] for i in range(0, len(plaintext), num_columns)]
    
    # Add padding if necessary (to make the last row the same length as key)
    last_row_length = len(grid[-1])
    if last_row_length < num_columns:
        grid[-1] += "X" * (num_columns - last_row_length)  # Pad with X
    
    # Read characters column by column in the order of the key
    ciphertext = ""
    for index in key_order:
        for row in grid:
            ciphertext += row[index]
    
    return ciphertext

# Function to decrypt using Keyed Transposition Cipher
def keyed_transposition_decrypt(ciphertext, key):
    key = key.upper()  # Make sure the key is in uppercase
    key_order = get_key_order(key)
    
    # Determine number of columns and rows
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns
    
    # Create a grid to store decrypted message
    grid = [''] * num_rows
    
    # Prepare an array of empty strings to hold columns
    columns = [''] * num_columns
    
    # Fill the columns according to the key order
    idx = 0
    for index in key_order:
        for row in range(num_rows):
            columns[index] += ciphertext[idx]
            idx += 1
    
    # Reconstruct the grid row by row from the filled columns
    for row in range(num_rows):
        for col in range(num_columns):
            grid[row] += columns[col][row]
    
    # Join rows and remove any padding (X's) at the end
    plaintext = ''.join(grid).rstrip('X')
    
    return plaintext

# Example Usage
message = "nishatmahmud"
key = "KEYWORD"

print("Original Message:", message)
ciphertext = keyed_transposition_encrypt(message, key)
print("Encrypted Message:", ciphertext)
decrypted_message = keyed_transposition_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)