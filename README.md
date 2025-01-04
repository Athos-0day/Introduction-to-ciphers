# Introduction to ciphers
---

In this repository, I share my work on the book **Breaking codes with python**. This is not my first time on python, but I chose this book to learn the basics of ciphers and learn how to make a plan to break a number. There is also the historical side that interests me.

Python is the best programming language for working on ciphers and cryptographic algorithms. Python's high-level data structures, such as lists, dictionaries, and tuples, are great for handling cryptographic data like keys, nonces, and ciphertext. 

For each cipher, we will work on a user interface and the goal is to hack a file which is encrypted, or just decrypted or encrypted a file with the key. 

## Transposition cipher

Dans cet algorithme, on élabore un anagramme du mot initial, car en effet, on altère la position des caractères et non leurs valeurs.

### Intéressons-nous à un exemple :

Prenons la phrase suivante : 
> "Le travail d'une génération commence ici"

La longueur de cette citation est de 40 caractères, les valeurs de clés possibles sont comprises entre 1 et 40. Prenons par exemple 9. La première étape consiste à écrire la phrase dans un tableau de 7 colonnes.

Voici comment la phrase serait répartie sur un tableau de 9 colonnes :

| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|----|----|----|----|----|----|----|----|----|
| L  | e  | *  | t  | r  | a  | v  | a  | i  |
| l  | *  | d  | '  | u  | n  | e  | *  | g  |
| é  | n  | é  | r  | a  | t  | i  | o  | n  |
| *  | c  | o  | m  | m  | e  | n  | c  | e  |
| *  | i  | c  | i  | -  | -  | -  | -  | -  |

En lisant colonne par colonne, on peut déduire le message chiffré. Il est important de noter que les `*` sont des espaces et les `-` sont des espaces non utilisés.

Le message chiffré est alors :  
> **"Llé**e*nci*déoct'rmiruamanteveina*ocigne"  



