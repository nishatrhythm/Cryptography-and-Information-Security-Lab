<h1 align="center">Cryptography and Information Security Lab</h1>

Welcome to the **Cryptography and Information Security Lab** repository. This repository covers a variety of classical and modern encryption algorithms, as well as cryptographic techniques for secure data transmission. Each algorithm is implemented in Python, and you can explore the code to understand how these cryptographic techniques work.

---

## Substitution Ciphers

### 1. Affine Cipher
The Affine Cipher is a type of monoalphabetic substitution where each letter in the alphabet is mapped to its numeric equivalent, encrypted using a mathematical function, and then converted back to a letter.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/AffineCipher.py)
- **Output**:
```
Original Message: nishatmahmud
Encrypted Message: VWURIZQIRQEX
Decrypted Message: NISHATMAHMUD
```

### 2. AutoKey Cipher
The AutoKey Cipher is a polyalphabetic substitution cipher where the key is extended by appending the message itself after the initial key.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/AutoKeyCipher.py)
- **Output**:
```
Original Message: nishatmahmud 
Encrypted Message: XMQDOKPNPEBD
Decrypted Message: NISHATMAHMUD
```

### 3. Caesar Cipher
The Caesar Cipher is one of the simplest and most widely known encryption techniques, in which each letter in the plaintext is shifted by a fixed number of positions.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/CaesarCipher.py)
- **Output**:
```
Original Message: nishatmahmud 
Encrypted Message: QLVKDWPDKPXG
Decrypted Message: NISHATMAHMUD
```

### 4. Playfair Cipher
The Playfair Cipher is a digraph substitution cipher where pairs of letters are encrypted together using a square matrix key.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/PlayfairCipher.py)
- **Output**:
```
Original Message: nishatmahmud 
Encrypted Message: AGPBRSORCOZC
Decrypted Message: NISHATMAHMUD
```

### 5. Vigenère Cipher
The Vigenère Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/VigenereCipher.py)
- **Output**:
```
Original Message: nishatmahmud 
Encrypted Message: XMQDOKPKLKQR
Decrypted Message: NISHATMAHMUD
```

---

## Transposition Ciphers

### 1. Keyed Transposition Cipher
In the Keyed Transposition Cipher, the order of characters in the plaintext is shifted based on a predetermined key.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/KeyedTranspositionCipher.py)
- **Output**:
```
Original Message: nishatmahmud
Encrypted Message: SMIHMXTXHUADNA
Decrypted Message: NISHATMAHMUD
```

### 2. Keyless Transposition Cipher
The Keyless Transposition Cipher reorders the plaintext without the use of a key, typically in a fixed pattern.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/KeylessTranspositionCipher.py)
- **Output**:
```
Original Message: nishatmahmud 
Encrypted Message: NAHITMSMUHAD
Decrypted Message: NISHATMAHMUD
```

---

## Symmetric Encryption Algorithms

### 1. Data Encryption Standard (DES)
DES is a block cipher that uses symmetric keys for encryption. It was one of the most widely used encryption algorithms in the past.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/DataEncryptionStandard.py)
- **Output**:
```
Plain Text:  0110000101100010011000110110010001100101011001100110011101101000 
Cipher Text:  0110000101100010011000110110010001100101011001100110011101101000
```

### 2. Advanced Encryption Standard (AES)
AES is a modern block cipher used for secure data encryption and is one of the most widely used cryptographic algorithms today.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/AdvancedEncryptionStandard.py)
- **Output**:
```
Plain Text:  abcdefghijklmnoq
Cipher Text:  62818f39118e69105b68315b7b30807d
```

### 3. Feistel Cipher
The Feistel Cipher structure is used in many symmetric block ciphers, splitting the data block and processing it through several rounds of encryption.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/FeistelCipher.py)
- **Output**:
```
Original Plaintext: 0XABCD1234
Encrypted Ciphertext: 0XDEF0EF81
Decrypted Plaintext: 0XABCD1234
```

### 4. Multiplicative Cipher
The Multiplicative Cipher uses a multiplication operation on the numeric equivalents of the letters of the alphabet for encryption.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/MultiplicativeCipher.py)
- **Output**:
```
Original Message: nishatmahmud 
Encrypted Message: NOMJARIAJIWP
Decrypted Message: NISHATMAHMUD
```

---

## Asymmetric Encryption Algorithms

### 1. Diffie-Hellman Key Exchange
Diffie-Hellman is a key exchange algorithm that allows two parties to securely share a secret key over an insecure channel.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/DiffieHellmanKeyExchange.py)
- **Output**:
```
Publicly shared values: p = 23, g = 5
Alice's private key: 6
Alice's public key: 8
Bob's private key: 15
Bob's public key: 19
Alice's computed shared secret: 2
Bob's computed shared secret: 2
Shared secret successfully computed: 2
```

### 2. ElGamal Algorithm
The ElGamal Algorithm is an asymmetric key encryption algorithm for public-key cryptography based on the Diffie-Hellman key exchange.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/ElGamalAlgorithm.py)
- **Output**:
```
Public key (p, g, y): (23, 5, 8), Private key (x): 6
Original message: 13
Encrypted message (c1, c2): (19, 3)
Decrypted message: 13
```

### 3. RSA Encryption
RSA is one of the first practical public-key cryptosystems and is widely used for secure data transmission.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/RSAencryption.py)
- **Output**:
```
Public key (e, n): (65537, 3233), Private key (d, n): (2753, 3233)
Original message: 42
Encrypted message (ciphertext): 2557
Decrypted message: 42
```

### 4. Rabin Cryptosystem
The Rabin Cryptosystem is an asymmetric algorithm that is similar to RSA but relies on different mathematical principles.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/RabinCryptosystem.py)
- **Output**:
```
Public key (n): 77, Private keys (p, q): (7, 11)
Original message: 5
Encrypted message (ciphertext): 25
Decrypted possible messages: (16, 61, 72, 5)
```

---

## Signature and Authentication Algorithms

### 1. Digital Signature Standard (DSS)
DSS is a suite of standards used for the generation and verification of digital signatures to ensure the authenticity of a message.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/DigitalSignatureStandard.py)
- **Output**:
```
Public key (p, q, g, y): (23, 11, 4, 2), Private key (x): 6
Signature for message 'nishat': (r, s) = (8, 5)
The signature for message 'nishat' is valid.
```

### 2. Secure Hash Algorithm 512-bit (SHA-512)
The SHA-512 (Secure Hash Algorithm 512-bit) is a cryptographic hash function designed to take an input and produce a 512-bit (64-byte) hash value, ensuring the integrity of the input data.
- **Code**: [See the code](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/SHA512.py)
- **Output**:
```
Original Message: This is a test message for SHA-512
SHA-512 hash of the predefined string: 9440af2a41a3ebb65de4f8bb75a2b50b66bb11bd677b5fc3cc431a804b449a751454b7adaeaf1a230a1eb358e4239e27dd64c272f5854a18c9f21f881eaaeb90
```

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab.git
```

2. Navigate to the specific folder where the desired algorithm is located.
3. Run the script using Python:
```bash
python <script_name>.py
```

---

## License

This repository is licensed under the MIT License. For more details, refer to the [LICENSE file](https://github.com/nishatrhythm/Cryptography-and-Information-Security-Lab/blob/main/LICENSE).
