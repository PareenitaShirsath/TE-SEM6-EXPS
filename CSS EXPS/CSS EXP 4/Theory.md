# A. C. Patil College of Engineering, Kharghar
## Department of Artificial Intelligence & Data Science  
### Academic Year 2024-25 (Even Sem.)  

[www.acpce.org](www.acpce.org)

## EXPERIMENT NO. 4  
### **Write a program to demonstrate the integrity of a message using MD5/SHA-1**  

---

## **AIM**  
Write a program to demonstrate the integrity of a message using MD5/SHA-1.

## **OBJECTIVE**  
- Able to implement MD5/SHA-1 algorithm.

## **OUTCOMES**  
- Implemented MD5/SHA-1 algorithm successfully.

---

## **THEORY**  
### **ALGORITHM DESCRIPTION**  
- The **MD5 message-digest algorithm** is a widely used cryptographic hash function producing a **128-bit (16-byte) hash value**, typically expressed in text format as a **32-digit hexadecimal number**.
- MD5 has been utilized in a wide variety of cryptographic applications and is also commonly used to **verify data integrity**.

### **MD5 Algorithm Steps**  
We begin with a **b-bit message** as input, and the goal is to find its message digest.

### **Step 1: Append Padding Bits**  
- The message is "padded" so that its length (in bits) is congruent to **448 modulo 512**.
- Padding includes a single **"1"** bit, followed by **"0"** bits until the length reaches **448 bits modulo 512**.

### **Step 2: Append Length**  
- A **64-bit representation** of `b` (message length before padding) is appended.
- The message length is now an **exact multiple of 512 bits**.

### **Step 3: Initialize MD Buffer**  
A four-word buffer **(A, B, C, D)** is used:
- `A = 0x67452301`
- `B = 0xefcdab89`
- `C = 0x98badcfe`
- `D = 0x10325476`

### **Step 4: Process Message in 16-Word Blocks**  
#### **Four Auxiliary Functions:**  
- `F(X,Y,Z) = (X AND Y) OR (NOT(X) AND Z)`
- `G(X,Y,Z) = (X AND Z) OR (Y AND NOT(Z))`
- `H(X,Y,Z) = X XOR Y XOR Z`
- `I(X,Y,Z) = Y XOR (X OR NOT(Z))`

#### **Processing Steps:**  
1. Process each 16-word block.
2. Save initial values of `A, B, C, D`.
3. Perform **four rounds** of operations.
4. Update buffer values:  
   ```
   A = A + AA
   B = B + BB
   C = C + CC
   D = D + DD
   ```

### **Step 5: Output**  
- The final message digest consists of **A, B, C, D** in hexadecimal format.

---

## **CONCLUSION**  
The **MD5/SHA-1 algorithm** has been successfully implemented to demonstrate the **integrity of a message**. The computed hash can be used to verify **data integrity** and detect any modifications.


