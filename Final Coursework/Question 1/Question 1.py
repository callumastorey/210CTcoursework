###QUESTION 1###
import random

givenList = [1,2,3,4,5,6,7,8]

def arrayShuffle(list):
    """Function to randomly shuffles an array of integers"""
    list2 = []
    for i in range(len(list)): # For every element in list
        addToList = random.choice(list) # Select  random item from givenList and add to variable
        list.remove(addToList) # Removing the currently selected element(held in addToList) from the original list
        list2.insert(i,(addToList)) # Adding the currently selected element(held in addToList) to the new list
    return list2 # Return newly created list, with random order of integers

print(arrayShuffle(givenList)) # Printing the newly created array

"""Description"""

"""This is a function to take a set of integers and randomly shuffle the array without the use of the
random.shuffle argument. The rationale is quite simple, im randomly selecting elements from the
original storing it in a variable, removing that specific element from the original list, so not
to be selected again. Then I am adding the, still selected, element and adding to a new list. This
is being put through a for statement, for each element in the list."""

"""Big O Notation"""

"""The Big O notation is 0(n)"""
