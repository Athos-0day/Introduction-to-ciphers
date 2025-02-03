import re
#This file is my implementation of the makeWordPatterns

def makeWordPattern(word) :
    #give a word and the function return his pattern 
    #for example : "test" -> 0.1.2.0
    num = 0 
    pattern = []
    letter_num = {}
    for letter in word :
        if letter not in letter_num :
            letter_num[letter] = num 
            num +=1
        
        pattern.append(str(letter_num[letter]))

    return '.'.join(pattern)


def makeDictPatterns() :
    #We now make a dict of pattern so we will found easily the pattern of each word in the dictionnary
    DictPattern = {}

    with open('Introduction-to-ciphers/dictionary.txt', 'r') as dictio:
            wordList = dictio.read().splitlines()

    for word in wordList :

        pattern = makeWordPattern(word)

        if pattern not in DictPattern :
            DictPattern[pattern] = []
        
        DictPattern[pattern].append(word)

    return DictPattern  

def get_words_from_string(text):
    # Remplacer les caractères non alphabétiques (hors des lettres et espaces) par des espaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Cela garde uniquement les lettres et les espaces
    words = text.split()  # Découpe la chaîne en mots
    words_lower = [word.lower() for word in words]  # Met tous les mots en minuscule
    return words_lower

def makeMessagePatterns(message) :
    wordlist = get_words_from_string(message)

    WordToPatternDict = {}

    for word in wordlist :
        WordToPatternDict[word] = makeWordPattern(word)
    
    return WordToPatternDict

