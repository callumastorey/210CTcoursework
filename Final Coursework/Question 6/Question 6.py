__author__ = 'Callum'
"""Write the pseudocode and code for a function that reverses
the words in a sentence. Input: "This is awesome"
Output: "awesome is This". Give the Big O notation."""

#split string into words using split.word(might have to change to something else

reverseString = "This is awesome"
#print(reverseString)
reverseString = reverseString.split()
#print(reverseString)

#reverse list
reverseString.reverse()
#print(reverseString)
reverseString = " ".join(reverseString)


#print list
print(reverseString)


#big o notation

