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

# Step 1: Key Generation
def generate_keys():
    # Choose two prime numbers (small values for simplicity, use larger primes in real use)
    p = 61
    q = 53
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Public exponent (commonly used value is 65537)
    e = 65537
    
    # Compute the private key 'd' (modular inverse of e modulo phi_n)
    d = mod_inverse(e, phi_n)
    
    # Public key is (e, n) and private key is (d, n)
    return e, d, n

# Step 2: Encryption (Public key is (e, n), plaintext is m)
def encrypt(m, e, n):
    return mod_exp(m, e, n)

# Step 3: Decryption (Private key is (d, n), ciphertext is c)
def decrypt(c, d, n):
    return mod_exp(c, d, n)

# Example Usage
if __name__ == "__main__":
    # Generate keys
    e, d, n = generate_keys()
    print(f"Public key (e, n): ({e}, {n}), Private key (d, n): ({d}, {n})")
    
    # Sample message (must be smaller than n)
    m = 42
    print(f"Original message: {m}")
    
    # Encrypt the message
    c = encrypt(m, e, n)
    print(f"Encrypted message (ciphertext): {c}")
    
    # Decrypt the ciphertext
    decrypted_message = decrypt(c, d, n)
    print(f"Decrypted message: {decrypted_message}")