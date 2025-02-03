import os, sys, HackSubstitution

#Enter the file you want to encrypt and the key
File = (input("What is the file that you want to hack with the substitution cipher ? \n"))


#Now we need to know if the file exist 
if not os.path.exists(File) :
    print('The file %s does not exist, you need to choose a file that exist.' % (File) )
    sys.exit


ReturnFile = ""
ReturnFile = File + '.H'


#We need to pay attention if the file already exist
Sure = ""
if os.path.exists(ReturnFile) :
    print("The file that you want to hack already exists : %s " % (ReturnFile))
    print("Do you want to write on it ? ")
    Sure = input("If you're sure write Yes : ")
    if not Sure.startswith("Yes") :
        sys.exit()

#The next step is to open the file and take the information that we need 
CurrentFile = open(File)
Content = CurrentFile.read()
CurrentFile.close()

lettermapping = HackSubstitution.HackSubMap(Content)
cleartext = HackSubstitution.DecryptWithCipherletterMapping(Content,lettermapping)

# Write the new content to the output file
with open(ReturnFile, 'w') as NewFile:
    NewFile.write(cleartext)

print("The new file is finished.")
print("Hack is complete!")