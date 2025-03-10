# **Implementation of Diffie-Hellman Key Exchange Algorithm**

## **AIM**  
Implementation of the Diffie-Hellman Key Exchange Algorithm.

## **OBJECTIVE**  
To implement the Diffie-Hellman Key Exchange Algorithm.

## **OUTCOMES**  
Successfully implemented the Diffie-Hellman Key Exchange Algorithm.

---

## **THEORY**  

### **ALGORITHM DESCRIPTION**  
- The **Diffie-Hellman (D-H) key exchange** is a secure method for exchanging cryptographic keys over a public channel.  
- It was one of the first **public-key protocols** and remains widely used today.  
- The Diffie-Hellman method allows two parties **without prior knowledge of each other** to securely establish a **shared secret key** over an insecure communication channel.  
- Once established, this **shared secret key** can be used for encrypting further communications using **symmetric key ciphers**.  

---

## **ALGORITHM**  

### **Global Public Elements**  
- Let **q** be a prime number.  
- Let **α** be a primitive root of **q**, where **α < q**.  

### **User A Key Generation**  
1. Select a **private key X**, where **X < q**.  
2. Calculate the **public key R1** using:  
   \[
   R1 = α^X \mod q
   \]
3. Share the **public key R1** with **User B**.  

### **User B Key Generation**  
1. Select a **private key Y**, where **Y < q**.  
2. Calculate the **public key R2** using:  
   \[
   R2 = α^Y \mod q
   \]
3. Share the **public key R2** with **User A**.  

### **Session Key Calculation**  
1. **User A computes the secret key K:**  
   \[
   K = (R2)^X \mod q
   \]  

2. **User B computes the secret key K:**  
   \[
   K = (R1)^Y \mod q
   \]  

Since both users compute the same value, **K serves as the shared secret key**.  

---

## **CONCLUSION**  
The **Diffie-Hellman Key Exchange Algorithm** allows two users to establish a **shared secret key** over an insecure channel without transmitting the key itself.  
This method is a **fundamental technique in modern cryptographic systems** and forms the basis for secure communications, such as in SSL/TLS protocols.  
The experiment provided insight into **public-key cryptography** and its role in secure key distribution.  

