###QUESTION 6###

givenStr = "This is awesome"

def sentReverse(string):
    """Function to reverse the order of a given string"""
    string = string.split() # Splits the string into a list
    string.reverse() # Reverses the order of the list
    string = " ".join(string) # Joins the elements of the list together with a space inbwtween the words, to form a str
    return string # Returns the reversed string

print(sentReverse(givenStr))

"""Pseudocode"""

"""
FUNCTION sentReverse(INPUT):
    INPUT = INPUT.SPLIT()
    INPUT.REVERSE()
    INPUT.JOIN(INPUT)
    RETURN

PRINT(sentReverse(INPUT))
"""

"""Description"""
"""This is another simple function that takes a given string and reverses the order of the words and returns.
The program first splits the string into a list, each word in its own element. The list is then reversed
using the list.reverse function, we then join the list back together to form a string then return."""

"""Big O Notation"""
"""The big o notation for this question is 0(1)"""

