#Decryption of the transposition cipher

#Retrieve the information
print("Give a key value and the associated ciphertext")
Key = int(input("The value of the key: "))
CipherText = input("The message you want to decrypt: ")

def DecryptTranspo(CipherText,Key) :

    #Initialisation of the values
    Length = len(CipherText)
    Rows = 0
    Columns = 0
    Novalue = Key*((Length//Key)+1) - Length
    PlainText = [""] * ((Length//Key)+1)

    for Caracters in CipherText :
        PlainText[Columns] += Caracters
        Columns += 1

        if Columns==((Length//Key)+1) or (Columns==(Length//Key) and Rows>=(Key-Novalue)) :
            Columns = 0 
            Rows +=1

    Message = ""
    for val in PlainText :
        Message += val
    return Message

print("The plaintext is : ")
print(DecryptTranspo(CipherText,Key))