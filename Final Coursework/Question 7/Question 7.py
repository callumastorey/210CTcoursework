__author__ = 'Callum'
'''Write a recursive function (pseudocode and code) to check if a number n is prime (hint:
check whether n is divisible by any number below n).'''

#take number



"""def primeNoChecker:
    for number in number:
        primeNo2 = primeNo2-

        if primeNo / primeNo2 ="""

"""def primeNoChecker(primeNo):
    #check that the prime number is more than 1
    if primeNo <= 1:
        return("Not Applicabable")
    #check that the no is more than the lowest prime number
    else:
        if 2 >= primeNo:
            print(primeNo)
        else:
            if primeNo == 2:
#if primeNo it is
#else
"""

primeNo = int(input(("Type an integer: ")))

def primeNoChecker(primeNo, primeDiv):
    if primeDiv == 1:
        return True
    else:
        if primeNo % primeDiv ==0:
            return False
        else:
            return primeNoChecker(primeNo,primeDiv-1)




if (not primeNoChecker(primeNo,primeNo-1)):
    print ("this number is not a  prime number")

else:
    print("this number is a prime numeber")
#try dividing by other numbers


#make recursive


#if prime say

