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

# Diffie-Hellman Key Exchange
def diffie_hellman():
    # Step 1: Agree on a large prime number (p) and a base (g)
    p = 23  # A small prime number for simplicity, use a large prime in real scenarios
    g = 5   # A primitive root modulo p

    print(f"Publicly shared values: p = {p}, g = {g}")

    # Step 2: Alice chooses a private key
    a_private = 6  # Alice's private key (this should be kept secret)
    print(f"Alice's private key: {a_private}")

    # Alice computes her public key and sends it to Bob
    a_public = mod_exp(g, a_private, p)
    print(f"Alice's public key: {a_public}")

    # Step 3: Bob chooses a private key
    b_private = 15  # Bob's private key (this should be kept secret)
    print(f"Bob's private key: {b_private}")

    # Bob computes his public key and sends it to Alice
    b_public = mod_exp(g, b_private, p)
    print(f"Bob's public key: {b_public}")

    # Step 4: Alice and Bob compute the shared secret
    # Alice computes the shared secret using Bob's public key and her private key
    shared_secret_alice = mod_exp(b_public, a_private, p)
    print(f"Alice's computed shared secret: {shared_secret_alice}")

    # Bob computes the shared secret using Alice's public key and his private key
    shared_secret_bob = mod_exp(a_public, b_private, p)
    print(f"Bob's computed shared secret: {shared_secret_bob}")

    # The shared secrets should be the same for both Alice and Bob
    if shared_secret_alice == shared_secret_bob:
        print(f"Shared secret successfully computed: {shared_secret_alice}")
    else:
        print("Error: Shared secrets do not match!")

# Run the Diffie-Hellman key exchange example
if __name__ == "__main__":
    diffie_hellman()