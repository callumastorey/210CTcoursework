__author__ = 'Callum'
"""Write a recursive function (pseudocode and code) that removes all vowels from a given string s.
Input: "beautiful" Output: "btfl"."""

#create dict with vowels

vowels = ['a','e','i','o','u']
#print(vowels)
#take word, convert to list
chosenWord = str(input("Type in a word: "))
#print(chosenWord)
#print(chosenWord)

"""
vowels      ----> list with vowels
chosenWord  ----> List of letters in word


def removeVowels():
    if vowel is in chosenWord:
        chosen

"""

"""
newList = chosenWord-vowels
print(newList)

#ITERATIVE FUNTION
#numberOfLetters = len(chosenWord)
#for i in range(0,numberOfLetters):

position <- 0
found <- False
while position < len(List) and not found:
    if List[position] = item:
        found <- True
    position <- position + 1"""




def removeVowels(I,chosenWord, vowels):
    if I>4:
        return chosenWord
    for x in chosenWord:
        #run linear search to find item in list
        if x == vowels[I]:
             chosenWord = chosenWord.replace(vowels[I], "")

    return removeVowels(I+1, chosenWord, vowels)



print(removeVowels(0,chosenWord,vowels))



""""
def LinearSearch(chosenWord, vowels):
    found = false
    position = 0
    while position < len(vowels and not found):
        if vowels[position == chosenWord]"""




#check word for vowels MAIN FUNCTION RECURSIVE

#def removeVowels():
 #   if vowels isnt in


#remove vowels from word
#print word
