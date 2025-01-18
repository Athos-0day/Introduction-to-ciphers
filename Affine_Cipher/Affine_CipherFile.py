import euclide
import os
import sys

Char = "ABCDEFGHIJKLMNQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .?!,"
LenSymbol = len(Char)

Mykey = int(input("What is your key? "))
Mode = input("Do you want to (E)ncrypt or (D)ecrypt? ")
File = input("What is the file you want to encrypt/decrypt with the affine cipher? \nThe file must have a .txt extension: ")

# Check if the file exists
if not os.path.exists(File):
    print(f"The file {File} does not exist. Please choose a valid file.")
    sys.exit(1)

ReturnFile = ""
if Mode == 'D':
    ReturnFile = File + ".D"
else:
    ReturnFile = File + ".E"

Sure = ""
if os.path.exists(ReturnFile):
    print(f"The file you want to {Mode} already exists: {ReturnFile}")
    print("Do you want to overwrite it?")
    Sure = input("If you're sure, type 'Yes' to overwrite: ")
    if not Sure.lower().startswith("yes"):
        print("Exiting without overwriting.")
        sys.exit(1)

# Open the file and read its content
with open(File, 'r') as CurrentFile:
    Content = CurrentFile.read()

# Functions for key generation, encryption, and decryption
def MakeKey(key: int):
    keyA = key // LenSymbol
    keyB = key % LenSymbol
    return (keyA, keyB)

def EncryptAffine(key: int, message):
    (keyA, keyB) = MakeKey(key)
    if euclide.gcd(keyA, LenSymbol) != 1:
        print("The key is not valid for the affine cipher (it must be coprime with the symbol length).")
        sys.exit(1)

    EncryptMessage = ""
    for val in message:
        if val in Char:
            index = Char.find(val)
            EncryptMessage += Char[(index * keyA + keyB) % LenSymbol]
        else:
            EncryptMessage += val
    return EncryptMessage

def DecryptAffine(key: int, message):
    (keyA, keyB) = MakeKey(key)
    DecryptMessage = ""
    ModInv = euclide.modInverse(keyA, LenSymbol)
    if ModInv is None:
        print("No modular inverse exists for the key, decryption is impossible.")
        sys.exit(1)

    for symbol in message:
        if symbol in Char:
            index = Char.find(symbol)
            DecryptMessage += Char[(index - keyB) * ModInv % LenSymbol]
        else:
            DecryptMessage += symbol
    return DecryptMessage

# Perform encryption or decryption
if Mode.startswith('D'):
    NewText = DecryptAffine(Mykey, Content)
elif Mode.startswith('E'):
    NewText = EncryptAffine(Mykey, Content)
else:
    print("You chose a mode that does not exist. Please try again with (D)ecrypt or (E)ncrypt.")
    sys.exit(1)

# Write the new content to the output file
with open(ReturnFile, 'w') as NewFile:
    NewFile.write(NewText)

print("The new file is finished.")

