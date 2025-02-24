# Implementation and Analysis of RSA Cryptosystem / Digital Signature Scheme using RSA/El Gamal

## Theory

### RSA Cryptosystem
RSA (Rivest-Shamir-Adleman) is an asymmetric encryption algorithm used for secure data transmission. It is based on the mathematical difficulty of factoring large prime numbers.

**Steps in RSA Encryption and Decryption:**
1. Select two large prime numbers, \( p \) and \( q \).
2. Compute \( n = p \times q \) (modulus).
3. Calculate Euler’s totient function, \( \phi(n) = (p-1) \times (q-1) \).
4. Choose an encryption key \( e \) such that \( 1 < e < \phi(n) \) and \( e \) is coprime with \( \phi(n) \).
5. Compute the decryption key \( d \) such that \( (d \times e) \mod \phi(n) = 1 \).
6. Encryption: \( C = M^e \mod n \) (where \( M \) is the plaintext message).
7. Decryption: \( M = C^d \mod n \).

### Digital Signature using RSA
A digital signature provides authentication, integrity, and non-repudiation using RSA. The sender encrypts a hash of the message with their private key, and the receiver decrypts it with the sender’s public key to verify the signature.

**Steps for Digital Signature:**
1. Compute the hash of the message.
2. Encrypt the hash using the sender’s private key to generate the signature.
3. Transmit the message along with the signature.
4. The receiver decrypts the signature using the sender’s public key.
5. The receiver computes the hash of the received message and compares it with the decrypted hash to verify integrity.

### El Gamal Cryptosystem
El Gamal is another asymmetric encryption algorithm based on the discrete logarithm problem, commonly used for digital signatures.

**Steps in El Gamal Digital Signature:**
1. Choose a large prime \( p \) and a generator \( g \).
2. Select a private key \( x \) and compute the public key \( y = g^x \mod p \).
3. Generate a random number \( k \) and compute signature values:
   - \( r = g^k \mod p \)
   - \( s = (H(m) - x \times r) \times k^{-1} \mod (p-1) \)
4. The receiver verifies the signature using \( r \) and \( s \).

## Conclusion

The implementation and analysis of the **RSA Cryptosystem** and **Digital Signature Schemes** using RSA/El Gamal highlight the importance of asymmetric cryptography in secure communication. RSA ensures confidentiality and authentication, while digital signatures provide integrity and non-repudiation. These cryptographic techniques are widely used in modern security applications such as SSL/TLS, secure email, and blockchain.

