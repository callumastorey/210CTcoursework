###QUESTION 2###

usersInt = (int(input("Give me an integer: ")))

def factorial(n):
    """Function to work out the factorial of a number"""
    i = 1
    while n >= 1:  # Keep looping while int being used is above or equal to 1, factorials do not get multiplied by 0
        i = i * n # The multiplication of 'i' with the iteratively reduced 'n' the main calculation with factorials
        n = n - 1 # N - 1 so that the factorial can proceed down the next multiplication level
    return i  # Returning the i integer which holds the final result of the calculations, the factorial of the given int

def trailingZeros(n):
    """Function to count the number of trailing zeros in a number"""
    counter = 0  # Setting the counter for number of 0s found within the number in a variable
    while n % 10 == 0:  # While the number can receive no remainder on a mathematical division by 10
        n = n / 10 # Dividing the factorial number by 10
        counter = counter + 1 # Keeping track of the number of times that it has been divided
    return counter  # Returning the total times the given number has been divided by returning the counter variable

factorialNumber = factorial(usersInt)
trailing = trailingZeros(factorialNumber)
print("The Factorial number is: " + str(factorialNumber))
#print(factorialNumber)
print("The number of trailing zeros is: " + str(trailing))

"""Description"""

"""This is a program to count the number of trailing zeros from a factorial number. I decided to use 2 functions
to split up the calculations. The first function works out the factorial of a given number. This is calculated
using an iterative method of multiplying the given integer against an integer of the same value, then each time
the loop is run, deducting 1 from the latter. This returns the factorial of a number. The second function takes
the factorial and using the modulus operator iteratively divides by 10 till it cant without resulting in a
remainder. A counter is ran within the loop and is then returned at the end. This counter is the indication
of how many trailing 0s are present in the factorial number."""

"""Big O Notation"""

"""The Big O notation is 0(n)"""
