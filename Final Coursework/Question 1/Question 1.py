__author__ = 'Callum'

import random

#CREATE LIST
list = [5,3,8,6,1,9,2,7]
list2 = []

#FOR EVERY I IN LIST


#ANOTHER METHOD
#print(random.choice(list))
#ADD RANDOM CHOICE TO LIST2
#list2.insert((random.choice(list)))

for i in range(0,8):
    addToList = random.choice(list)
    list.remove(addToList)
    #randomListLocation = random.randint(0,7)
    #list2.insert((randomListLocation),(addToList))
    list2.insert(i,(addToList))


print(list2)

#o notation is n

