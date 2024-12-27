#The goal is to hack the Transposition cipher 
#We will use the brute force method but we will adapt it to make it faster and easier for the user to know which is the good text
import time, os, StatEnglish, sys

#Take the file to brute force 
File = input("What is the name of the file that you want to brute force ? \nThe File need to have a .txt extension : ")

#We need to look if the file exist or not
if not os.path.exists(File) :
    print('The file %s does not exist, you need to choose a file that exist.' % (File) )
    sys.exit

#Next step is to open the file 
CurrentFile = open(File)
Content = CurrentFile.read()
CurrentFile.close()

NumberOfKey = len(Content)
Verification = False 
KeyNumber = 1

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

while KeyNumber<=NumberOfKey and not Verification :

    Text = DecryptTranspo(Content,KeyNumber) 

    if StatEnglish.StatEnglish(Text)>=0.20 :
        print()
        print(Text)
        print()
        S = input("Is it the plaintext ? Y or N ")
        if S.startswith('Y') :
            Verification = True
    
    KeyNumber += 1
    

if KeyNumber>NumberOfKey :
    print()
    print("Failed to hack encryption")

else :
    print()
    print("The hack succeed")
    print("The file used the transpoition encryption with the key %s" % (KeyNumber-1))
    returnFile = File + '.H'
    print("Writing in the %s file..." % (returnFile))
    NewFile = open(returnFile,'w')
    NewFile.write(Text)
    NewFile.close()     






