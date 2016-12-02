###QUESTION 8###

vowels = ['a','e','i','o','u']
givenWord = str(input("Type in a word: "))

def removeVowels(counter,givenWord, vowels):
    """Function to remove vowels from a given word"""
    if counter > 4: # If counter is more than 4, it means that there are no vowels remaining in chosenWord
        return givenWord
    for i in givenWord: # For each character in chosenWord
        if i == vowels[counter]: # If character matches the currently selected vowel
             givenWord = givenWord.replace(vowels[counter], "") # Remove the currently selected vowel from chosenWord
    return removeVowels(counter+1, givenWord, vowels) # Return to beginning of function, +1 counter for next vowel
print(removeVowels(0,givenWord,vowels))

"""Pseudocode"""

"""
INPUT = vowels
INPUT = STRING

FUNCTION removeVowels(counter, INPUT, vowels):
    IF counter > 4:
        RETURN INPUT
    FOR I IN INPUT:
        IF I = vowels[counter]:
            INPUT = INPUT.REMOVE(vowel)
    RETURN removeVowels(counter-1, INPUT, vowels)
PRINT(removeVowels(0, INPUT, vowels)

"""

"""Description"""
"""This recursive program removes vowels from a given string. A vowel list is given to the program and each
time the function runs a different vowel is compared to each character in the given word. A counter is used
 to track when all the vowels have been searched for."""

"""Big O Notation"""
"""The big o notation for this question is 0(n)"""
