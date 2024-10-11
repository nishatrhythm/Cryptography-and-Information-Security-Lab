# Helper function: Modular Exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # Divide the exponent by 2
        base = (base * base) % mod  # Square the base
    return result

# Helper function: Extended Euclidean Algorithm to find the modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m

# Step 1: Key Generation
def generate_keys():
    # Choose a large prime number (small prime for simplicity, use large in real scenarios)
    p = 23
    g = 5   # Primitive root modulo p
    
    # Private key (x) is a random number between 1 and p-2
    x = 6  # Alice's private key (this should be kept secret)
    
    # Public key (y = g^x mod p)
    y = mod_exp(g, x, p)
    
    # Public key is (p, g, y) and private key is (x)
    return p, g, y, x

# Step 2: Encryption (Public key is (p, g, y), plaintext is m)
def encrypt(m, p, g, y):
    k = 15  # Random ephemeral key chosen by the sender (should be random each time)
    
    # Compute c1 = g^k mod p
    c1 = mod_exp(g, k, p)
    
    # Compute c2 = m * y^k mod p
    c2 = (m * mod_exp(y, k, p)) % p
    
    return c1, c2

# Step 3: Decryption (Private key is x, ciphertext is (c1, c2))
def decrypt(c1, c2, p, x):
    # Compute the shared secret c1^x mod p
    s = mod_exp(c1, x, p)
    
    # Compute the modular inverse of s mod p
    s_inv = mod_inverse(s, p)
    
    # Decrypt the message m = c2 * s_inv mod p
    m = (c2 * s_inv) % p
    
    return m

# Example Usage
if __name__ == "__main__":
    # Generate keys
    p, g, y, x = generate_keys()
    print(f"Public key (p, g, y): ({p}, {g}, {y}), Private key (x): {x}")
    
    # Sample message (must be smaller than p)
    m = 13
    print(f"Original message: {m}")
    
    # Encrypt the message
    c1, c2 = encrypt(m, p, g, y)
    print(f"Encrypted message (c1, c2): ({c1}, {c2})")
    
    # Decrypt the ciphertext
    decrypted_message = decrypt(c1, c2, p, x)
    print(f"Decrypted message: {decrypted_message}")