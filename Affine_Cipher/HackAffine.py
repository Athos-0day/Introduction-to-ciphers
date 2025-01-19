import euclide, sys, os, StatEnglish

Char = "ABCDEFGHIJKLMNQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .?!,"
LenSymbol = len(Char)
Verification = False 

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

# Functions for key generation, encryption, and decryption
def MakeKey(key: int):
    keyA = key // LenSymbol
    keyB = key % LenSymbol
    return (keyA, keyB)

def DecryptAffine(key: int, message):
    (keyA, keyB) = MakeKey(key)
    DecryptMessage = ""
    ModInv = euclide.modInverse(keyA, LenSymbol)
    if ModInv is None:
        
        return None 

    for symbol in message:
        if symbol in Char:
            index = Char.find(symbol)
            DecryptMessage += Char[(index - keyB) * ModInv % LenSymbol]
        else:
            DecryptMessage += symbol
    return DecryptMessage

key = 0 
print("Hacking...")
while key<=(LenSymbol**2) and not Verification :
    Text = DecryptAffine(key,Content) 
    if Text is not None :
        if StatEnglish.StatEnglish(Text)>=0.20 :
            print()
            print(Text)
            print()
            S = input("Is it the plaintext ? Y or N ")
            if S.startswith('Y') :
                Verification = True
    
    key += 1
    

if not Verification :
    print()
    print("Failed to hack encryption")

else :
    print()
    print("The hack succeed")
    print("The file used the transpoition encryption with the key %s" % (key-1))
    returnFile = File + '.H'
    print("Writing in the %s file..." % (returnFile))
    NewFile = open(returnFile,'w')
    NewFile.write(Text)
    NewFile.close()     
