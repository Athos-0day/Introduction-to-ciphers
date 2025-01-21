import os, sys, SubstitutionCipher

#Enter the file you want to encrypt and the key
File = (input("What is the file that you want to encrypt/decrypt with the substitution cipher ? \n"))
Key = input("What is the key that you want to use ? ")

#Now we need to know if the file exist 
if not os.path.exists(File) :
    print('The file %s does not exist, you need to choose a file that exist.' % (File) )
    sys.exit

#Then we need to verify that the key is valid 
if not SubstitutionCipher.IsValidKey(Key) :
    print('The key %s is not valid' % (Key) )
    sys.exit

Mode = input("Do you want to (E)ncrypt or (D)ecrypt the file ? ")
ReturnFile = ""

if Mode=='D' :
    ReturnFile= File+".D"
else :
    ReturnFile = File +".E"


#We need to pay attention if the file already exist
Sure = ""
if os.path.exists(ReturnFile) :
    print("The file that you want to %a already exists : %s " % (Mode,ReturnFile))
    print("Do you want to write on it ? ")
    Sure = input("If you're sure write Yes : ")
    if not Sure.startswith("Yes") :
        sys.exit()

#The next step is to open the file and take the information that we need 
CurrentFile = open(File)
Content = CurrentFile.read()
CurrentFile.close()

if Mode.startswith('D') :
    print('You will decrypt your file with the key : %s' % (Key))
    NewText = SubstitutionCipher.DecryptSubstitution(Content,Key)
elif Mode.startswith('E') :
    print('You will encrypt your file with the key : %s' % (Key))
    NewText = SubstitutionCipher.EncryptSubstitution(Content,Key)
else : 
    print("You chose a mode that does not exist. Please try again with (D)ecrypt or (E)ncrypt.")
    sys.exit(1)

# Write the new content to the output file
with open(ReturnFile, 'w') as NewFile:
    NewFile.write(NewText)

print("The new file is finished.")

