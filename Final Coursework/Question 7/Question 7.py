###QUESTION 7###

givenInt = int(input(("Type an integer: ")))

def primeCheck(givenInt, primeDiv):
    """Function to check whether a given integer is a prime number or not"""
    if primeDiv == 1: # If the prime numbers division has reached 1 it cannot be divided by anything but 1 and itself
        return True # Return true, the number is prime
    else:
        if givenInt % primeDiv ==0: # If givenInt can be divided by primeDiv without leaving a remainder
            return False # If remainder is found the number can be divided by itself and other numbers, not prime
        else:
            return primeCheck(givenInt,primeDiv-1) # Recursively return to beginning of function

if (not primeCheck(givenInt,givenInt-1)): # If primecheck has not been returned, it is not a prime number
    print ("this number is not a  prime number")
else: # Else the number is prime
    print("this number is a prime number")

"""Pseudocode"""

"""
FUNCTION primeCheck(INPUT, primeDIV):
    IF primeDiv = 1:
        RETURN TRUE
    ELSE:
        IF INPUT % primeDiv = 0:
            RETURN FALSE
        ELSE:
            RETURN primeCheck(INPUT, primeDiv-1)

IF NOT primeCheck(INPUT,INPUT-1):
    RETURN FALSE
ELSE:
    RETURN TRUE
"""

"""Description"""
"""This recursive program checks if a given integer is prime. It works by taking a dividing variable
that on every recursive loop -1 from its value, meaning that the program is continuely counting down
through possible divisions till it reaches 1. If it reaches 1 the number is prime. However if it is
able to divide and leave no remainder the number is not a prime."""

"""Big O Notation"""
"""The big o notation for this question is 0(n)"""
