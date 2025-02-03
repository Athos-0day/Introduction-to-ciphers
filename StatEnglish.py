#This file let to create a dictionnary of english words 
#That is the goal of the first function 
def LoadDictionnary() :
    DictionnaryFile = open('dictionary.txt')
    EnglishDict = {}
    for word in DictionnaryFile.read().split('\n') :
        EnglishDict[word] = None
    DictionnaryFile.close()
    return EnglishDict

EnglishDict = LoadDictionnary()

#Then we need to remove all the value that we can't take in count for the verification 
#That is hte goal of the second function
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LettersAndSpace = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def RemoveNonLetters(Text) :
    lettersOnly = []
    for symbol in Text :
        if symbol in LettersAndSpace :
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

#Finally we count the numbers of words that are in the file and in the dictionnary
def StatEnglish(Text) :
    Text = Text.lower()
    Text = RemoveNonLetters(Text)
    ListOfWords = Text.split()

    if len(ListOfWords)==0 :
        return 0.0
    
    EnglishWords_Counts = 0

    for Value in ListOfWords :
        if Value in EnglishDict :
            EnglishWords_Counts+=1
    return float(EnglishWords_Counts)/len(ListOfWords)



