__author__ = 'Callum'
"""Given a sequence of n integer numbers, extract the sub-sequence of maximum length
which is in ascending order."""


givenList = [1,2,3,4,1,5,1,6,7]
#i = selected element in list
#j = next selected element in list



def sequenceFinder(givenList):
    newList = []
    for i in range(len(givenList)):
        n = 0
        p = 1
        if givenList[n] == givenList[p-1]:
            newList.append(givenList[n])
            n = n+1
            p = p+1
            #print(givenList)
            #print(newList)

        else:
            print("failed")
            return
    print(newList)
sequenceFinder(givenList)


#run linear search list


#compare two numbers next to each other


#if 2nd number is larger than the 1st add both to the new list


#contiue adding the same list if the next numbers are larger than the priors


#break when a smaller number occurs


#do this till the end of list


#compare all lists gathered from linear search


#output largest list
