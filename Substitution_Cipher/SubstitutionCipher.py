#In this file we can find the function we need to encrypt or decrypt a file

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#First we need to know if the key is valid
def IsValidKey(key) -> bool :
    KeyList = list(key)
    LetterList = list(Letters)
    KeyList.sort()
    return KeyList==LetterList

#This function take a message and encrypt it 
def EncryptSubstitution(Message,key) :
    CipherText = TranslateSubstitution(Message,key,'encrypt')
    return CipherText

#This function take a ciphertext and the key and return the plaintext
def DecryptSubstitution(Message,key) :
    PlainText = TranslateSubstitution(Message,key,'decrypt')
    return PlainText

def TranslateSubstitution(Message,key,mode) :
    TranslatedMessage = ''
    KeyA = Letters 
    KeyB = key

    if mode=='decrypt' :
        KeyA,KeyB = KeyB,KeyA
    
    for val in Message :
        if val.upper() in KeyA :
            index = KeyA.find(val.upper())
            if val.isupper() :
                TranslatedMessage += KeyB[index].upper() 
            else :
                TranslatedMessage += KeyB[index].lower()
        else :
            TranslatedMessage += val
    
    return TranslatedMessage



    
