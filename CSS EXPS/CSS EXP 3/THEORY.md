AIM:Implementation of Diffie Hellman Key exchange algorithm
OBJECTIVE: Able to implement Diffie Hellman Key exchange algorithm.
OUTCOMES: Implemented Diffie Hellman Key exchange algorithm.
THEORY:
ALGORITHM DESCRIPTION:
 Diffie–Hellman key exchange (D–H) is a specific method of securely exchanging
cryptographic keys over a public channel and was one of the first public-key protocols.
 The Diffie–Hellman key exchange method allows two parties that have no prior
knowledge of each other to jointly establish a shared secret key over an insecure
channel.
 This key can then be used to encrypt subsequent communications using a symmetric key
cipher.

ALGORITHM
Global Public Elements:
Let q be a prime number and α where α &lt; q and α is a primitive root of q.
User A Key Generation:
Select private X where X &lt; q
Calculate public R1 where R1 = α X mod q
Share public key R1 with user B
User B Key Generation:
Select private Y whereY &lt; q
Calculate public R2 where R2 = α Y mod q
Share public key R2 with user A

1. Calculation of Secret Key by User A (Session Key)
K = (R2)α X mod q
2. Calculation of Secret Key by User B:(Session Key)
K = (R1)α Y mod q

CONCLUSION:
