# Introduction to ciphers

In this repository, I share my work on the book **Breaking codes with python**. This is not my first time on python, but I chose this book to learn the basics of ciphers and learn how to make a plan to break a number. There is also the historical side that interests me.

Python is the best programming language for working on ciphers and cryptographic algorithms. Python's high-level data structures, such as lists, dictionaries, and tuples, are great for handling cryptographic data like keys, nonces, and ciphertext. 

For each cipher, we will work on a user interface and the goal is to hack a file which is encrypted, or just decrypted or encrypted a file with the key. 

## Transposition cipher

In this algorithm, we develop an anagram of the initial word, because indeed, we alter the position of the characters and not their values.

### Let’s look at an example :

Let’s take the following sentence : 
> "Le travail d'une génération commence ici"

The length of this quote is 40 characters, the possible key values are between 1 and 40. Take 9 for example. The first step is to write the sentence in a table of 7 columns.

The sentence would be divided into a table of 9 columns as follows:

| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|----|----|----|----|----|----|----|----|----|
| L  | e  | *  | t  | r  | a  | v  | a  | i  |
| l  | *  | d  | '  | u  | n  | e  | *  | g  |
| é  | n  | é  | r  | a  | t  | i  | o  | n  |
| *  | c  | o  | m  | m  | e  | n  | c  | e  |
| *  | i  | c  | i  | -  | -  | -  | -  | -  |

Reading column by column, the encrypted message can be deduced. It is important to note that the `*`s are spaces and the `-`s are unused spaces.

The encrypted message is then:  
> **"Llé**e*nci*déoct'rmiruamanteveina*ocigne"  

## The Affine Cipher

The **Affine Cipher** is a substitution cipher method where each letter of the message is replaced by another according to an affine function. This affine function is defined by two parameters: **\(a\)** and **\(b\)**. The affine cipher is a simplified form of symmetric key encryption, using mathematical operations on the positions of characters in the alphabet.

### How the Affine Cipher Works

The affine cipher relies on the application of an affine function in modular algebra. The encryption formula is as follows:

![Affine Encryption Formula](https://latex.codecogs.com/svg.latex?E(x)%20=%20(a%20\cdot%20x%20+%20b)%20%5Cmod%20m%bg=transparent)

Where:
- \(E(x)\) is the encrypted character at position \(x\) in the alphabet.
- \(a\) and \(b\) are the keys of the affine cipher, where:
  - \(a\) must be an integer such that **\(a\)** and **\(m\)** (the length of the alphabet) are coprime (i.e., \(\text{gcd}(a, m) = 1\)).
  - \(b\) is an integer that shifts the character within the alphabet.
- \(m\) is the total number of symbols in the alphabet used (e.g., 26 for the Latin alphabet without accents).

#### Example of Encryption
Let’s consider a simple alphabet with the 26 letters of the Latin alphabet:

\[
\text{Alphabet} = \{A, B, C, ..., Z\}
\]

If we choose \(a = 5\) and \(b = 8\), the encryption function becomes:

![Example Encryption Formula](https://latex.codecogs.com/svg.latex?E(x)%20=%20(5%20\cdot%20x%20+%208)%20%5Cmod%2026%bg=transparent)

Where \(x\) is the position of each letter in the alphabet. For example:

- To encrypt the letter **A** (which is at position 0 in the alphabet), we apply the formula:
  \[
  E(0) = (5 \cdot 0 + 8) \mod 26 = 8 \quad \Rightarrow \quad \text{the encrypted letter is H}
  \]
  
- To encrypt the letter **B** (position 1), we apply the formula:
  \[
  E(1) = (5 \cdot 1 + 8) \mod 26 = 13 \quad \Rightarrow \quad \text{the encrypted letter is N}
  \]

This process continues for each letter in the message.

### Decryption of the Affine Cipher

Decryption of the affine cipher requires the inverse of the affine function, which involves using the modular inverse of \(a\), denoted \(a^{-1}\). The decryption formula is then:

![Affine Decryption Formula](https://latex.codecogs.com/svg.latex?D(y)%20=%20a^{-1}%20\cdot%20(y%20-%20b)%20\mod%20m%bg=transparent)

Where:
- \(D(y)\) is the decrypted position of the encrypted character \(y\).
- \(a^{-1}\) is the modular inverse of \(a\) modulo \(m\), i.e., a number such that \(a \cdot a^{-1} \equiv 1 \mod m\).
- \(b\) is the same value used in encryption.

#### Example of Decryption
Let’s revisit the example where \(a = 5\) and \(b = 8\). To decrypt, we need the modular inverse of \(a = 5\) modulo 26, which is \(a^{-1} = 21\) (because \(5 \cdot 21 \equiv 1 \mod 26\)).

Let’s say we have an encrypted message, for example, "H" (which corresponds to position 7 in the alphabet). To decrypt it, we apply the formula:

![Decryption Example](https://latex.codecogs.com/svg.latex?D(7)%20=%2021%20\cdot%20(7%20-%208)%20\mod%2026%20=%2021%20\cdot%20(-1)%20\mod%2026%20=%2021%20\cdot%2025%20\mod%2026%20=%2019%bg=transparent)

This gives us the letter **T**, which was the original letter before encryption.

### Conditions for Valid Use
For the affine cipher to work properly:
1. **\(a\)** must be invertible modulo \(m\), meaning \(\text{gcd}(a, m) = 1\). This ensures that \(a^{-1}\) exists.
2. The affine cipher is thus limited by this condition on \(a\), which restricts the possible choices for the key.

---



