###Question 9###
list = [2,3,5,7,9,13,16,19,25,34]
lowNo = 17
highNo = 22
l = 0
h = len(list)-1

def intvSearch(list,lowNo,highNo, l, h):
    """Function to find out whether an integer between given intervals exists"""
    while l <= h:
        mid = (int(l + h) //2) # mid = low + high returned with an even number usig the // operator
        if list[mid] >= lowNo and list[mid] <= highNo:
            print("True")
            return
        elif highNo <= list[mid]:
            return intvSearch(list,lowNo, highNo, l, mid-1) # Return to beginning of function midpoint - 1

        elif lowNo >= list[mid]:
            return intvSearch(list, lowNo, highNo, mid+1, h)
    print("False") # If able to exist loop, number has not been found within given range
print(list)
intvSearch(list,lowNo,highNo,l,h)

"""Pseudocode"""

"""
INPUT list
INPUT lowNo
INPUT highNo
L = 0
H = LENGTH(list)-1

FUNCTION intvSearch(list, lowNo, highNo, 1, h):
            WHILE L <= H:
                mid = (L+H)//2
                IF list[mid] >= lowNo and list[mid] <= highNo:
                    TRUE
                    RETURN
                ELIF highNo <= list[mid]:
                    RETURN INTVSEARCH(list, lowNo, highNo, l ,mid-1):
                ELIF highNo <= list[mid]:
                    RETURN INTVSEARCH(list, lowNo, highNo, mid+1, h):

CALL INTVSEARCH

"""

"""Description"""
"""
This program is an adapted binary search algorithm that checks whether an integer between given intervals exists.

"""

"""Big O Notation"""
"""The big o notation for this question is 0(Log(n))"""
