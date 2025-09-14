# Matrix Encryption with Python  

This project implements a simple **matrix-based encryption and decryption system** using **linear algebra**.  
It converts a text message into a numerical matrix (via Unicode values), encrypts it using a **randomly generated invertible key matrix**, and allows decryption using the inverse of that key.  

The encryption adds extra complexity by transposing the encrypted matrix before converting it back into text.  

---

## ✨ Features
- Encrypt and decrypt text messages using **3×3 matrix transformations**.  
- Key is generated as a **3×3 matrix of Unicode Greek/Coptic characters (880–1023)**.  
- Ensures key matrix is **invertible** (determinant ≠ 0).  
- Automatic message padding with `{` so message length is always a multiple of 3.  

---

## ⚙️ How It Works
1. Message is converted into a matrix of Unicode values.  
2. The key (3×3 matrix) is applied as a **linear transformation**.  
3. The result is transposed for additional complexity.  
4. The encrypted matrix is converted back into text.  
5. Decryption reverses the process using the **inverse key matrix**.  

---

## 📦 Requirements

Install dependencies:
pip install -r requirements.txt