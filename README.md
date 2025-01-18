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
