import LettersMapping, SubstitutionCipher, re, FindWordsPatterns

nonLettersorSpacePattern = re.compile('[^A-Z\s]')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def HackSubMap(message) : 
    intersectMap = LettersMapping.MakeBlankLetterMapping()
    cipherwordlist = re.sub(nonLettersorSpacePattern, '', message.upper()).split()

    dictpattern = FindWordsPatterns.makeDictPatterns()

    for cipherword in cipherwordlist :

        candidatemap = LettersMapping.MakeBlankLetterMapping()

        cipherwordpattern = FindWordsPatterns.makeWordPattern(cipherword)

        if cipherwordpattern in dictpattern :
            candidatemap = LettersMapping.WordLetterMapping(cipherword,dictpattern,candidatemap)
    
        intersectMap = LettersMapping.IntersectLetterMapping(intersectMap,candidatemap)

    return RemoveSolvedLettersFromMapping(intersectMap)

#It's a copy of the program you can found in the book
def RemoveSolvedLettersFromMapping(letterMapping):
    
    # Cipherletters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)

    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # `solvedLetters` will be a list of uppercase letters that have one
        # and only one possible mapping in `letterMapping`:
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, than it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again.
                        loopAgain = True
    return letterMapping

def DecryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    return SubstitutionCipher.DecryptSubstitution(ciphertext,key)


