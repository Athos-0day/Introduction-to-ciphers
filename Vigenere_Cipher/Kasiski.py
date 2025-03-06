#The goal of this file is to implement the Kasiski method
import re
from collections import Counter

#This function aims to find the patterns of size n and retrieve the one with the highest frequency
def find_pattern(text, patternLength=3) :
    # First step: keep only the relevant characters (letters)
    filtered_text = re.sub(r'[^a-zA-Z]', '', text)
    workText = filtered_text.upper() # Convert everything to uppercase

    patternDict = {}
    positionPatterndict = {}
    text_length = len(workText)

    # Iterate through the text
    for index in range(text_length-patternLength + 1) :
        
        # Update the dictionaries
        if workText[index:index+patternLength] in patternDict :
            patternDict[workText[index:index+patternLength]] += 1
            positionPatterndict[workText[index:index+patternLength]].append(index)
        else :
            patternDict[workText[index:index+patternLength]] = 1
            positionPatterndict[workText[index:index+patternLength]] = [index]
    
    if len(patternDict)==0 :
        return False
    
    finalDict = {}
    # Remove patterns that appear only once
    for pattern in patternDict :
        if patternDict[pattern] > 1 :
            finalDict[pattern] = positionPatterndict[pattern]

    return finalDict


#this function calculates the distance between patterns
def calculate_distance(positionPatterndict : dict) :
    distances = {}

    if len(positionPatterndict)==0 :
        return False
    
    for patterns in positionPatterndict :
        n = len(positionPatterndict[patterns])
        dist_list = []
        for i in range(n-1) :
            dist_list.append(positionPatterndict[patterns][i+1] - positionPatterndict[patterns][i])
        
        distances[patterns] = dist_list
    
    return distances 

#finding common factors in distances
def find_factors(distances) :
    all_distances = []

    if len(distances)==0 :
        return False

    # Merge all distances in a list
    for dist_list in distances.values():
        all_distances.extend(dist_list)
            
    # Count the frequency of each distance
    distance_frequency = Counter(all_distances)

    # Find common factors
    factors = []
    for dist, count in distance_frequency.items():
        if count > 1:  # We keep only the repeated distances
            factors.append(dist)
    
    return factors

#finaly this is the Kasiski method
def kasiski_method(text) :

    # Find patterns and their positions
    positionPatterndict = find_pattern(text)

    if not positionPatterndict :
        return "No repeats found to break the encryption."

    # Calculate the distances between pattern positions
    distances = calculate_distance(positionPatterndict)

    if not distances:
        return "No calculated distance between repetitions."

    # Find common factors in distances
    factors = find_factors(distances)

    if not factors:
        return "No common factor found to estimate key length."
    # Find the key length
    key_length = min(factors)

    return key_length

