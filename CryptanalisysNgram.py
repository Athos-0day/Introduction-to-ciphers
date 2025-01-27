#The goal is to make four functions 
#The first is a simple frenquence analysis of a file  
#The second one is to produce a picture of this analysis
#The third one is the same thing but for 2-gram

import matplotlib.pyplot as plt
import string

#classic frequency analysis
def frenquencyanalysis(text) -> dict :
    frenquence_dict = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
    'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
    'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}
    
    textmaj = text.upper()

    for val in textmaj :
        if val in frenquence_dict :
            frenquence_dict[val] += 1 
    
    return frenquence_dict

# English letter frequencies (approximate percentages)
english_letter_freq = {
    'A': 8.12, 'B': 1.49, 'C': 2.23, 'D': 4.25, 'E': 12.02, 'F': 1.98, 
    'G': 1.48, 'H': 6.09, 'I': 7.31, 'J': 0.09, 'K': 0.77, 'L': 4.03, 
    'M': 2.02, 'N': 6.95, 'O': 7.68, 'P': 1.93, 'Q': 0.10, 'R': 5.99, 
    'S': 6.28, 'T': 9.10, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 
    'Y': 1.97, 'Z': 0.07
}

def plot_frequency_analysis_from_dict(frequency_dict: dict):
    # Prepare data for the plot
    letters = list(frequency_dict.keys())
    frequencies = list(frequency_dict.values())

    # Normalize the text frequencies (convert to percentages)
    total_letters = sum(frequencies)
    normalized_text_frequencies = [(freq / total_letters) * 100 for freq in frequencies]

    # Get the English frequencies for comparison
    english_frequencies = [english_letter_freq.get(letter, 0) for letter in letters]

    # Create the plot
    plt.figure(figsize=(12, 6))  # Set figure size
    plt.bar(letters, normalized_text_frequencies, width=0.4, label="Text Frequencies", align='center', color='skyblue')
    plt.bar(letters, english_frequencies, width=0.4, label="English Frequencies", align='edge', color='orange')

    # Add titles and labels
    plt.title("Comparison of Text Letter Frequencies with English Frequencies", fontsize=14)
    plt.xlabel("Letters", fontsize=12)
    plt.ylabel("Frequency (%)", fontsize=12)
    plt.xticks(rotation=90)
    plt.legend()
    
    # Show the plot
    plt.show()

#frequency analysis of 2-grams

# English digraph frequencies (approximate percentages)
english_digram_freq = {
    'TH': 3.56, 'HE': 3.28, 'IN': 2.70, 'ER': 2.61, 'AN': 2.49, 'RE': 2.40,
    'ND': 2.27, 'AT': 2.18, 'ON': 2.14, 'NT': 2.10, 'HA': 2.04, 'ES': 1.97,
    'ST': 1.90, 'EN': 1.88, 'ED': 1.87, 'TO': 1.86, 'IT': 1.83, 'OU': 1.80,
    'EA': 1.74, 'HI': 1.71, 'IS': 1.69, 'OR': 1.64, 'TI': 1.63, 'AS': 1.59,
    'TE': 1.57, 'ET': 1.55, 'OF': 1.53, 'LY': 1.49, 'SA': 1.47, 'SE': 1.44
}

def plot_digram_frequency_analysis(frequency_dict: dict):
    # Prepare the data for plotting
    digrams = list(frequency_dict.keys())
    frequencies = list(frequency_dict.values())

    # Normalize text digram frequencies to percentage
    total_digrams = sum(frequencies)
    normalized_text_frequencies = [(freq / total_digrams) * 100 for freq in frequencies]

    # Get the English digram frequencies for comparison
    english_frequencies = [english_digram_freq.get(digram, 0) for digram in digrams]

    # Create the plot
    plt.figure(figsize=(12, 6))  # Set figure size
    plt.bar(digrams, normalized_text_frequencies, width=0.4, label="Text Frequencies", align='center', color='skyblue')
    plt.bar(digrams, english_frequencies, width=0.4, label="English Frequencies", align='edge', color='orange')

    # Add titles and labels
    plt.title("Comparison of Text Digram Frequencies with English Digram Frequencies", fontsize=14)
    plt.xlabel("Digrams", fontsize=12)
    plt.ylabel("Frequency (%)", fontsize=12)
    plt.xticks(rotation=90)
    plt.legend()
    
    # Show the plot
    plt.show()

def digram_frequency_analysis(text: str) -> dict:
    # Initialize a dictionary to store digram frequencies
    digram_freq = {}

    # Convert text to uppercase and remove non-alphabetic characters
    text_upper = ''.join([char.upper() for char in text if char.isalpha()])

    # Extract digrams and count their frequencies
    for i in range(len(text_upper) - 1):
        digram = text_upper[i:i+2]  # Get two consecutive letters
        if digram in digram_freq:
            digram_freq[digram] += 1
        else:
            digram_freq[digram] = 1

    return digram_freq




