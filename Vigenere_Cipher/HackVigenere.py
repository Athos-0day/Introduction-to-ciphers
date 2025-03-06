import VigenereCipher, Kasiski
from collections import Counter

# Analyze subtexts and apply frequency analysis
def frequency_analysis(text, key_length=3):
    subtexts = ['' for _ in range(key_length)]
    
    for i, char in enumerate(text):
        subtexts[i % key_length] += char
    
    # Calculate the frequency of each letter in each subtext
    frequencies = []
    for subtext in subtexts:
        subtext_freq = Counter(subtext)
        frequencies.append(subtext_freq)

    return frequencies


# Main function of the Kasiski method
def kasiski_analysis_and_decrypt(text):    
    # Estimate key length
    key_length = Kasiski.kasiski_method(text)

    if not key_length:
        return "Unable to determine the key length."
    
    # Analyze subtexts and apply frequency analysis
    frequencies = frequency_analysis(text,key_length)
    
    return frequencies

# Function to deduce the key from the frequency analysis
def deduce_key(frequencies):
    # The most frequent letter in English is 'E'
    most_frequent_letter = 'E'
    key = []
    
    # For each subtext, calculate the key letter
    for subtext_freq in frequencies:
        # Find the most frequent letter in the subtext
        most_common_letter, count = subtext_freq.most_common(1)[0]
        
        # Calculate the shift of this letter compared to 'E'
        shift = (ord(most_common_letter) - ord(most_frequent_letter)) % 26
        key.append(shift)
    
    # Convert the list of shifts (numbers) to letters to form the final key
    key_string = ''.join([chr(k + ord('A')) for k in key])  # Convert numbers to letters
    
    return key_string

# Main function for the complete analysis
def vigenere_key_decryption(text, key_length):
    # Perform the frequency analysis
    frequencies = frequency_analysis(text, key_length)
    
    # Deduce the key from the frequency analysis
    key = deduce_key(frequencies)
    
    return key

def hack_vigenere(text) :
    key_length = Kasiski.kasiski_method(text)
    key = vigenere_key_decryption(text,key_length)
    
    #hackText = VigenereCipher.DecryptVigenere(text,key)

    return key

