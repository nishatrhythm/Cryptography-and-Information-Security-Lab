# Playfair Cipher Encryption and Decryption

# Function to generate 5x5 Playfair cipher key matrix
def generate_key_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace J with I (common in Playfair Cipher)
    key_matrix = []
    used_letters = set()

    for char in key:
        if char not in used_letters and char.isalpha():
            key_matrix.append(char)
            used_letters.add(char)

    # Add remaining letters to the matrix
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # 'J' is omitted
        if char not in used_letters:
            key_matrix.append(char)
            used_letters.add(char)

    # Return as a 5x5 matrix
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

# Function to split message into digraphs (pairs of letters)
def prepare_message(message):
    message = message.upper().replace('J', 'I')  # Replace J with I
    digraphs = []
    i = 0
    while i < len(message):
        char1 = message[i]
        if i + 1 < len(message):
            char2 = message[i + 1]
            if char1 != char2:
                digraphs.append(char1 + char2)
                i += 2
            else:
                digraphs.append(char1 + 'X')  # Insert X between repeated letters
                i += 1
        else:
            digraphs.append(char1 + 'X')  # Add X if the last letter is single
            i += 1
    return digraphs

# Function to find the position of a letter in the key matrix
def find_position(char, key_matrix):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

# Encryption function
def encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    digraphs = prepare_message(plaintext)
    ciphertext = ""

    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], key_matrix)
        row2, col2 = find_position(digraph[1], key_matrix)

        # Same row: Shift right
        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5]
            ciphertext += key_matrix[row2][(col2 + 1) % 5]
        # Same column: Shift down
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1]
            ciphertext += key_matrix[(row2 + 1) % 5][col2]
        # Rectangle swap
        else:
            ciphertext += key_matrix[row1][col2]
            ciphertext += key_matrix[row2][col1]

    return ciphertext

# Decryption function
def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""

    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], key_matrix)
        row2, col2 = find_position(digraph[1], key_matrix)

        # Same row: Shift left
        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5]
            plaintext += key_matrix[row2][(col2 - 1) % 5]
        # Same column: Shift up
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1]
            plaintext += key_matrix[(row2 - 1) % 5][col2]
        # Rectangle swap
        else:
            plaintext += key_matrix[row1][col2]
            plaintext += key_matrix[row2][col1]

    return plaintext

# Example Usage
key = "MONARCHY"
message = "nishatmahmud"
print("Original Message:", message)
ciphertext = encrypt(message, key)
print("Encrypted Message:", ciphertext)
decrypted_message = decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)