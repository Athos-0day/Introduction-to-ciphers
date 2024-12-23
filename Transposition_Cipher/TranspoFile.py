import os, sys, string 

#The goal of this program is to Encrypt or Decrypt a file by using the Transposition Cipher
#First thing is to know what the user whant
#I will use the main function for the next cipher !

File = (input("What is the file that you want to encrypt/decrypt with the transposition cipher ? \nThe File need to have a .txt extension : "))
Key = int(input("What is the key that you want to use ? "))

#Now we need to know if File exists
if not os.path.exists(File) :
    print('The file %s does not exist, you need to choose a file that exist.' % (File) )
    sys.exit

#The goal is to write the plaintext or ciphertext in an other file 
#We need to know if the user want to decrypt or encrypt the file 
#And then we need to know if the file where we want to write already exists

Mode = input("Do you want to (E)ncrypt or (D)ecrypt your file ? ")
ReturnFile = ""

if Mode=='D' :
    ReturnFile= File+".D"
else :
    ReturnFile = File +".E"

Sure = ""
if os.path.exists(ReturnFile) :
    print("The file that you want to %a already exists : %s " % (Mode,ReturnFile))
    print("Do you want to write on it ? ")
    Sure = input("If you're sure write Yes : ")
    if Sure.startswith("Yes") :
        sys.exit()

#The next step is to open the file and take the information that we need 
CurrentFile = open(File)
Content = CurrentFile.read()
CurrentFile.close()

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

def EncryptTranspo(Message,Key) :

    #variable initialization 
    Length = len(Message)
    k = 0
    n = 0
    EncryptMessage = ""

    while n<Key :
        while k<=(Length//Key) :
            
            if (n+k*Key)<Length :
                EncryptMessage += Message[n+k*Key]
            k+=1
        
        k=0
        n+=1
    return EncryptMessage

#Now we need to encrypt or decrypt the file 
if Mode.startswith('D') :
    NewText = DecryptTranspo(Content,Key)
elif Mode.startswith('E') :
    NewText = EncryptTranspo(Content,Key)
else :
    print("You choose a mode that does not exist, please try again with (D)ecrypt or (E)ncrypt")
    sys.exit()

#Then write the new content in the new file 
NewFile = open(ReturnFile,'w')
NewFile.write(NewText)
NewFile.close()

print("The new file is finished")



    
