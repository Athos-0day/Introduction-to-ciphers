#This is an implementation of the Vigenere Cipher 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def VigenereCipher(message,key,mode) :
    index = 0 
    translated = []
    key = key.upper()

    for symbol in message :

        num = LETTERS.find(symbol)

        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[index]) # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[index]) # Subtract if decrypting.

            num %= len(LETTERS)

            # Add the encrypted/decrypted symbol to the end of translated:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            index += 1 # Move to the next letter in the key.
            if index == len(key):
                index = 0
        else:
            # Append the symbol without encrypting/decrypting.
            translated.append(symbol)

    return ''.join(translated)

def DecryptVigenere(message,key) :
    return VigenereCipher(message,key,'decrypt')

def EncryptVigenere(message,key) :
    return VigenereCipher(message,key,'encrypt')
