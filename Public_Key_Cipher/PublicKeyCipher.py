import sys, math

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,\''

def BlockFromText(text, blockSize):
    # Take a text and a block size, and return a list of strings
    # where each string has a maximum length of blockSize
    BlockList = []

    n = len(text)
    maxBlockNumber = n // blockSize  # Number of full blocks

    for i in range(maxBlockNumber):
        BlockList.append(text[i * blockSize : (i + 1) * blockSize])  # Add full blocks

    # Add the last block if there's any remaining text
    if n % blockSize != 0:
        BlockList.append(text[maxBlockNumber * blockSize :])

    return BlockList

def BlockFromTextTest() :
    text = "Hello, this is a test sentence."
    blockSize = 10
    result = BlockFromText(text, blockSize)
    print(result)

def TextBlocktoIntBlock(BlockList, blockSize) :
    #Take a text block list and convert it to 
    #an integer block list

    blockInt = 0
    blockInts = []
    n = len(SYMBOLS)
    i = 0

    for textblock in BlockList :
        blockInt = 0

        for character in textblock :
            if character not in SYMBOLS:
                print('ERROR: The symbol set does not have the character %s' % (character))
                sys.exit()
            
            index = SYMBOLS.index(character)

            blockInt += index*(n**(i%blockSize))
            i+=1
        
        blockInts.append(blockInt)
        i = 0

    return blockInts

def getTextFromBlocks(blockInts, messageLength, blockSize):
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer:
                charIndex = blockInt // (len(SYMBOLS) ** i)
                blockInt = blockInt % (len(SYMBOLS) ** i)
                blockMessage.insert(0, SYMBOLS[charIndex])
        message.extend(blockMessage)
    return ''.join(message)

def BlockTest() :
    text = "Hello, this is a test sentence."
    blockSize = 10
    result = BlockFromText(text, blockSize)
    print(result)
    result2 = TextBlocktoIntBlock(result,blockSize)
    print(result2)
    result3 = getTextFromBlocks(result2,len(text),blockSize)
    print(result3)

def encryptMessage(message, publicKey, blockSize) :
    encryptedBlocks = []
    n,e = publicKey

    blockText = BlockFromText(message,blockSize)
    blockInts = TextBlocktoIntBlock(blockText,blockSize)

    for block in blockInts :
        encryptedBlocks.append(pow(block,e,n))
    return encryptedBlocks

def decryptMessage(encryptedBlocks,messageLength,privateKey, blockSize) :
    decryptedBlocks = []

    n,d = privateKey

    for block in encryptedBlocks :
        decryptedBlocks.append(pow(block,d,n))

    return getTextFromBlocks(decryptedBlocks,messageLength,blockSize)

def readKeyFile(keyFilename):
    # Given the filename of a file that contains a public or private key,
    # return the key as a (n,e) or (n,d) tuple value.
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))

def encryptAndwriteFile(keyFilename,messageFilename,message,blockSize=None) :

    #First step is to retrieve the key
    keySize,n,e = readKeyFile(keyFilename)

    if blockSize == None:
        # If blockSize isn't given, set it to the largest size allowed by the key size and symbol set size.
        blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))
    # Check that key size is large enough for the block size:
    if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('ERROR: Block size is too large for the key and symbol set size. Did you specify the correct key file and encrypted file?')

    #Second step is to encrypt the message
    encryptedBlocks = encryptMessage(message,(n,e),blockSize)

    # Convert the large int values to one string value:
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    # Write out the encrypted string to the output file:
    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()
    # Also return the encrypted string:
    return encryptedContent

def readAnddecryptFile(keyFileName,EncryptedFile) :
    #First step is to retrieve the key
    keySize,n,d = readKeyFile(keyFileName)

    #Second step is to open the file and 
    #Divide the information
    fo = open(EncryptedFile)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that key size is large enough for the block size:
    if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('ERROR: Block size is too large for the key and symbol set size. Did you specify the correct key file and encrypted file?')

    #Third step is decrypt the file 
    #So first we need to make the encrypted blocks
    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))
    
    return decryptMessage(encryptedBlocks,messageLength,(n,d),blockSize)

def main():
    while True:
        # Ask the user what action they want to perform
        print("Welcome to the encryption/decryption tool!")
        action = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").strip().lower()

        if action not in ['e', 'd']:
            print("ERROR: Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")
            continue
        
        # Request the key file name
        keyFilename = input("Enter the filename of the key (e.g., key.txt): ").strip()

        try:
            # If encrypting
            if action == 'e':
                message = input("Enter the message you want to encrypt: ").strip()
                messageFilename = input("Enter the filename to save the encrypted message (e.g., encrypted.txt): ").strip()
                
                # Optional block size
                blockSize = input("Enter the block size (press Enter to use default): ").strip()
                blockSize = int(blockSize) if blockSize else None
                
                # Encrypt and write the file
                encryptedContent = encryptAndwriteFile(keyFilename, messageFilename, message, blockSize)
                print(f"Message encrypted successfully. Encrypted content saved in '{messageFilename}'.")

            # If decrypting
            elif action == 'd':
                encryptedFilename = input("Enter the filename of the encrypted message to decrypt: ").strip()
                
                # Decrypt and show the result
                decryptedMessage = readAnddecryptFile(keyFilename, encryptedFilename)
                print(f"Decrypted message: {decryptedMessage}")

        except FileNotFoundError:
            print(f"ERROR: The file '{keyFilename}' or the encrypted file does not exist. Please check the file path.")
        except ValueError:
            print("ERROR: Invalid input! Please ensure that the key file and the encrypted file contain valid data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Ask if the user wants to perform another operation
        another_action = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if another_action != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()