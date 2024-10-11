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

# A simple hash function (in real DSA, SHA-1 or SHA-256 is typically used)
def hash_message(m):
    return sum(ord(c) for c in m) % q  # Simple hash function, in real DSS use SHA-1 or SHA-256

# Step 1: Key Generation
def generate_keys():
    # Choose large prime numbers (small values for simplicity)
    p = 23
    q = 11  # q divides p-1 (23-1 = 22)
    g = 4   # Generator g, typically 1 < g < p and g^q mod p = 1
    
    # Private key (x), 0 < x < q
    x = 6
    
    # Public key (y = g^x mod p)
    y = mod_exp(g, x, p)
    
    return p, q, g, y, x

# Step 2: Sign the message
def sign_message(m, p, q, g, x):
    k = 7  # Random ephemeral key, 0 < k < q
    H_m = hash_message(m)  # Hash of the message
    
    # Compute r = (g^k mod p) mod q
    r = mod_exp(g, k, p) % q
    
    # Compute s = k^-1 * (H(m) + x * r) mod q
    k_inv = mod_inverse(k, q)
    s = (k_inv * (H_m + x * r)) % q
    
    return r, s

# Step 3: Verify the signature
def verify_signature(m, r, s, p, q, g, y):
    H_m = hash_message(m)  # Hash of the message
    
    # Compute w = s^-1 mod q
    w = mod_inverse(s, q)
    
    # Compute u1 = H(m) * w mod q
    u1 = (H_m * w) % q
    
    # Compute u2 = r * w mod q
    u2 = (r * w) % q
    
    # Compute v = (g^u1 * y^u2 mod p) mod q
    v = (mod_exp(g, u1, p) * mod_exp(y, u2, p) % p) % q
    
    # The signature is valid if v == r
    return v == r

# Example Usage
if __name__ == "__main__":
    # Generate keys
    p, q, g, y, x = generate_keys()
    print(f"Public key (p, q, g, y): ({p}, {q}, {g}, {y}), Private key (x): {x}")
    
    # Sign a message
    m = "nishat"
    r, s = sign_message(m, p, q, g, x)
    print(f"Signature for message '{m}': (r, s) = ({r}, {s})")
    
    # Verify the signature
    is_valid = verify_signature(m, r, s, p, q, g, y)
    if is_valid:
        print(f"The signature for message '{m}' is valid.")
    else:
        print(f"The signature for message '{m}' is NOT valid.")