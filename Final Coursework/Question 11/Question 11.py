###QUESTION 11###

class Node(object):
    """The Class to hold and manage properties of a node"""
    def __init__(self, v, n = None, p= None):
        """Initializing the value(v) and Next Pointer(n) and Previous Pointer(p) of a linked list node"""
        self.value = v
        self.next = n
        self.prev = p
    def getNext (self):
        """Function to get the next pointer part of the node"""
        return self.next
    def setNext (self,n):
        """Function to set the next pointer to variable n"""
        self.next = n
    def getPrev (self):
        """Function to get the previous node pointer"""
        return self.prev
    def setPrev (self,p):
        """Function to set the pointer to variable p"""
        self.prev = p
    def getValue (self):
        """Function to get the value of the node"""
        return self.value
    def setValue (self,v):
        """Function to set the value of the node to variable v"""
        self.value = v

class List(object):
    """The class to display and manage the linked list"""
    def __init__(self,r = None):
        """Intializer for the beginning of the list (root(r)) and the size of the list"""
        self.root = r
        self.size = 0

    def getSize (self):
        """Function to get the size of the list"""
        return self.size

    def addNode(self, x):
        """Function to add node to list"""
        newNode = Node(x, self.root)
        if self.root: # If there is another node in the list
            self.root.setPrev(newNode)      # Assigning the root nodes previous node to the new node
        self.root = newNode
        self.size += 1

    def removeNode (self, x):
        """Function to remove node from list"""
        thisNode = self.root # getting current node to use for removal
        previousNode = None # getting previous node, for change of pointer
        while thisNode:
            if thisNode.getValue() == x:
                next = thisNode.getNext() # Setting the next pointer
                prev = thisNode.getPrev() # Setting the prev pointer

                if next:
                    next.setPrev(prev) # Setting the next nodes previous pointer to the nodes next pointer
                if prev:
                    prev.setNext(next) # Setting the previous nodes next pointer to the nodes previous pointer
                else:
                    self.root = thisNode
                self.size -= 1
                return print("Element has been removed from the list")
            else: # If not found in current mode, move to the next node
                previousNode = thisNode
                thisNode = thisNode.getNext()
        return print("The element does not exist") # The element does not exist

    def displayList(self):
        """Function to display the linked list"""
        node = self.root
        while node:
            value1 = node.getValue()
            print(value1)
            node = node.getNext()

linkedList = List()
linkedList.addNode(26)
linkedList.addNode(14)
linkedList.addNode(39)
linkedList.addNode(65)
linkedList.addNode(47)
print(linkedList.removeNode(45))
print(linkedList.removeNode(39))
linkedList.displayList()

"""Description"""
"""With this question I was tasked with adding a node delete function to a double linked list.
I ended up changing the majority of the given code, and splitting lots of parts into individual
functions, giving me much better modularity and expandability. I have 2 classes, one for the node
properties and the other for displaying the list.
"""

"""Big O Notation"""
"""The big o notation for this question is 0(n^2)"""
