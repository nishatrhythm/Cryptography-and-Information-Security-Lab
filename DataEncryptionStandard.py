# Initial Permutation (IP) table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation (FP) table (Inverse of IP)
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# A simple key for illustration (64-bit binary string)
key = "1010101010111011000010010001100000100111001101101100110011011101"

# Function to apply permutation
def apply_permutation(input_text, table):
    return ''.join([input_text[i - 1] for i in table])

# Simple XOR function for two binary strings
def xor(a, b):
    return ''.join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])

# Simplified encryption function
def encrypt(plain_text):
    # Step 1: Initial Permutation
    permuted_text = apply_permutation(plain_text, IP)

    # Step 2: Split into two halves
    left = permuted_text[:32]
    right = permuted_text[32:]

    # Step 3: Simplified round function (normally 16 rounds, simplified here)
    for _ in range(16):
        temp = right
        right = xor(left, key[:32])  # XOR left half with the key (simplified)
        left = temp

    # Step 4: Combine left and right halves
    combined_text = left + right

    # Step 5: Final Permutation
    cipher_text = apply_permutation(combined_text, FP)

    return cipher_text

# Main execution
if __name__ == "__main__":
    # Example plain text (64-bit binary string)
    plain_text = "0110000101100010011000110110010001100101011001100110011101101000"  # "abcdefgh" in binary

    print("Plain Text: ", plain_text)

    # Encrypt the plain text
    cipher_text = encrypt(plain_text)

    print("Cipher Text: ", cipher_text)