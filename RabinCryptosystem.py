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
    # Prime numbers p and q (small values for simplicity, use larger primes in real-world use)
    p = 7
    q = 11
    n = p * q
    return p, q, n

# Step 2: Encryption (Public key is n, plaintext is m)
def encrypt(m, n):
    return mod_exp(m, 2, n)

# Step 3: Decryption (Private keys are p, q)
def decrypt(c, p, q, n):
    # Compute square roots modulo p and q
    mp = mod_exp(c, (p + 1) // 4, p)
    mq = mod_exp(c, (q + 1) // 4, q)
    
    # Use Chinese Remainder Theorem to get four possible plaintexts
    inv_q = mod_inverse(q, p)
    inv_p = mod_inverse(p, q)
    
    x1 = (mp * q * inv_q + mq * p * inv_p) % n
    x2 = (mp * q * inv_q - mq * p * inv_p) % n
    
    # Return the four possible solutions
    return x1, n - x1, x2, n - x2

# Example Usage
if __name__ == "__main__":
    # Generate keys
    p, q, n = generate_keys()
    print(f"Public key (n): {n}, Private keys (p, q): ({p}, {q})")
    
    # Sample message (must be smaller than n)
    m = 5
    print(f"Original message: {m}")
    
    # Encrypt the message
    c = encrypt(m, n)
    print(f"Encrypted message (ciphertext): {c}")
    
    # Decrypt the ciphertext
    possible_messages = decrypt(c, p, q, n)
    print(f"Decrypted possible messages: {possible_messages}")