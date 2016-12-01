###QUESTION 3###

usersInt = int(input(("Type an integer: ")))

def highestPerfSqr(usersInt):
    """Function to find the highest perfect square root from a given integer"""
    result = usersInt**.5 # Finding the square root of the given number
    result = int(result) # Turning the float back to an integer rounds down to the nearest whole number
    result = result * result # Multiplying the result by itself to find the new square number
    return result # Returning the result

print(highestPerfSqr(usersInt))


"""Pseudocode"""

"""
INPUT = INPUT(int)

FUNCTION highestPerfSqr(I)
    RESULT = square root(I)
    RESULT = round down(I)
    RESULT = RESULT * RESULT
    RETURN RESULT

PRINT(highestPerfSqr(INPUT))
"""


"""Description"""
"""This is a function to find the highest perfect square number from a given integer. The theory is really
quite simple. All we really need to do is square root the given integer, we will most likely be returned
with an un-even float. With python you can easily round down to the nearest positive integer by changing
the variable from a float to an integer. Once it is an integer you can easily return the square root value
of that integer."""


"""Big O Notation"""
"""The big o notation for this question is 0(1)"""
