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



