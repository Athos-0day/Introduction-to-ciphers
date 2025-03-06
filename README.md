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

## Affine Cipher

The **Affine Cipher** is a type of monoalphabetic substitution cipher, where each letter in an alphabet is replaced by another based on a mathematical function. The cipher uses two keys: **\(a\)** and **\(b\)**, which are used to transform the plaintext into ciphertext.

### How it works

The encryption function takes the position of a letter in the alphabet (for example, A = 0, B = 1, ..., Z = 25), then applies a mathematical formula that uses two keys: \(a\) (a multiplier) and \(b\) (a shift). The resulting value is then mapped back to a letter in the alphabet.

To decrypt, the receiver applies the inverse of the function using the modular inverse of \(a\).

### Example

Let’s consider an example where we encrypt the word **"HELLO"** using the keys \(a = 5\) and \(b = 8\).

1. For **H** (position 7), we apply the formula to get the encrypted letter. This process is repeated for each letter in the word.
2. After applying the formula for all letters, we get the ciphertext **"RCLLA"**.

To decrypt, we apply the inverse of the encryption function using the modular inverse of \(a\), which gives us back the original word: **"HELLO"**.

### Key Conditions

- The multiplier \(a\) must be coprime with the number of letters in the alphabet (26 for English letters). This ensures that \(a\) has an inverse, which is needed for decryption.
- The key \(b\) can be any integer, and it simply shifts the letters.

### Limitations

- The Affine Cipher is vulnerable to **frequency analysis** because it is a substitution cipher, and frequent letters in the ciphertext can give clues about the plaintext.
- The number of possible key pairs is limited by the requirement that \(a\) must be coprime with 26, restricting the choices for the encryption keys.

### Key Takeaways

- The Affine Cipher is easy to implement and use, but it is not secure for large-scale encryption due to its vulnerability to attacks like frequency analysis.
- It provides a good introduction to basic encryption techniques and modular arithmetic in cryptography.

## Substitution Cipher

The **Substitution Cipher** is one of the oldest and simplest encryption methods, where each letter in the plaintext is replaced with another letter according to a fixed system or key. In the case of the **monoalphabetic substitution cipher**, each letter in the alphabet is replaced by a corresponding letter from a predefined key. The key is a permutation of the alphabet, where each letter is mapped uniquely to another letter in the alphabet, making the key a 26-character long string.

### How it works

For example, if the key is:  
`QWERTYUIOPASDFGHJKLZXCVBNM`

Then, the letter **A** in the plaintext would be replaced by **Q**, **B** by **W**, **C** by **E**, and so on. To encrypt a message, we simply replace each letter in the plaintext with the corresponding letter from the key. To decrypt, the reverse process is applied using the inverse of the key, where **Q** is replaced by **A**, **W** by **B**, and so on.

### Example

Let’s consider the message **"HELLO"** and the substitution key **`QWERTYUIOPASDFGHJKLZXCVBNM`**:

- **H** becomes **A**
- **E** becomes **Q**
- **L** becomes **B**
- **L** becomes **B**
- **O** becomes **S**

Thus, the encrypted message would be: **"AQBBS"**

This cipher provides a simple way to encrypt messages, but it can easily be broken with techniques like frequency analysis, especially when the cipher is applied to large amounts of text.

### Key Takeaways

- The Substitution Cipher is a simple encryption technique, but it offers limited security due to its vulnerability to frequency analysis.
- A key of length 26 means that each letter in the plaintext is substituted by another letter, and this permutation can be random or follow a specific pattern.
- While easy to implement, the Substitution Cipher is not secure for modern cryptographic needs, but it provides a good foundation for understanding the basics of encryption.

### How I hack the substitution cipher

The goal was to recognize the patterns of each word and compare them with words in the dictionary. Thus, one can find which letter of the key is associated with which letter of the alphabet. This way, you get a partial result of the clear text but it is quite simple to complete when the text is long enough.

## Vigenère Cipher 

### Introduction

The **Vigenère cipher** is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It uses a keyword where each letter of the plaintext is shifted by a number of positions in the alphabet based on the corresponding letter in the key. The Vigenère cipher is considered much more secure than the Caesar cipher because it uses multiple shifts rather than just one.

#### Encryption Process

To encrypt a message, the Vigenère cipher performs the following steps:

1. Repeat the key as many times as needed to match the length of the plaintext.
2. For each letter of the plaintext:
   - Shift the letter by the number corresponding to the matching letter in the key.
   - For example, if the key letter is `K`, the shift will be 10 positions forward (since `K` is the 11th letter of the alphabet, but zero-indexed).

The formula for encrypting each character is:

Where:
- `C(i)` is the encrypted character,
- `P(i)` is the plaintext character,
- `K(i)` is the key character (converted to a number),
- and the result is taken modulo 26 (the number of letters in the alphabet).

#### Decryption Process

To decrypt a message, the process is similar, but instead of shifting forward, you shift the characters backward by the value of the key letter.

### Cracking the Vigenère Cipher

The Vigenère cipher is vulnerable to cryptanalysis if the length of the key is short and the ciphertext is long enough. There are several methods to break the Vigenère cipher:

#### 1. **Kasiski Examination**

The Kasiski method is one of the most effective ways to break the Vigenère cipher. It works by looking for repeating patterns in the ciphertext. If a pattern repeats, it's likely that the same key has been used to encrypt both occurrences of the pattern. The distances between these repeating patterns can give us the length of the key.

Steps for Kasiski Examination:
- Look for repeating sequences in the ciphertext.
- Calculate the distance between each repetition.
- Find the factors of these distances, as the key length is likely to be one of these factors.

#### 2. **Frequency Analysis**

Once the key length is determined, the ciphertext can be divided into multiple subtexts. Each subtext corresponds to a different letter of the key. Then, a frequency analysis is performed on each subtext to determine the most frequent letters. In the English language, the most common letter is usually 'E'. By comparing the most frequent letter in each subtext with 'E', we can determine the shifts (i.e., the values of the key).

#### Example of Frequency Analysis:
1. Split the ciphertext into subtexts based on the key length.
2. Perform frequency analysis on each subtext.
3. The most frequent letter in each subtext will likely correspond to 'E' (in English).
4. Calculate the shift for each subtext, which corresponds to one letter of the key.

#### 3. **Brute Force (when the key length is small)**

If the key length is small, it's also possible to use a brute-force approach. This involves trying all possible combinations of keys and decrypting the ciphertext until a readable message is found.

### The Current Implementation

The goal of the current implementation is to automate the process of determining the key length using the Kasiski method and then applying frequency analysis to deduce the key. However, there is an issue with the current implementation.



