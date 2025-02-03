#In this file we will work on the link between letters and words patterns
import FindWordsPatterns

def MakeBlankLetterMapping() :
    return {'A': [],'B': [],'C': [],'D': [],'E': [],'F': [],'G': [],'H': [],'I': [],'J': [],'K': [],'L': [],'M': [],'N': [],'O': [],
    'P': [],'Q': [],'R': [],'S': [],'T': [],'U': [],'V': [],'W': [],'X': [],
    'Y': [],'Z': []}

def WordLetterMapping(word,Dict,letterMapping) :
    WordPattern = FindWordsPatterns.makeWordPattern(word)
    word = word.upper()

    if WordPattern in Dict :
        Canditates = Dict[WordPattern]
    
    for canditate in Canditates :
        canditate = canditate.upper()

        n = len(canditate)
        for i in range(n) :
            if canditate[i] not in letterMapping[word[i]] :
                letterMapping[word[i]].append(canditate[i])
    
    return letterMapping

def IntersectLetterMapping(lettermapping1,lettermapping2) :
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    lettermapping = {}

    for letter in LETTERS :
        if lettermapping1[letter] == [] :
            lettermapping[letter] = lettermapping2[letter]

        elif lettermapping2[letter] == [] :
            lettermapping[letter] = lettermapping1[letter]
        
        else :
            lettermapping[letter] = []

            for val in lettermapping1[letter] :
                for let in lettermapping2[letter] :
                    if val==let :
                        lettermapping[letter].append(val)
    
    return lettermapping






