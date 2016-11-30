__author__ = 'Callum'
# This is the class to establish the Node: Value and Pointer
class Node(object):
    # Initializer for the value(v) and Next Pointer(n) and Previous Pointer(p) of a linked list node
    def __init__(self, v, n = None, p= None):
        self.value = v
        self.next = n
        self.prev = p

    # Function to get the next pointer part of the node
    def getNext (self):
        return self.next
    # Function to set the next pointer to variable n
    def setNext (self,n):
        self.next = n

    # Function to get the previous node pointer
    def getPrev (self):
        return self.prev
    # Function to set the pointer to variable p
    def setPrev (self,p):
        self.prev = p

    # Function to get the value of the node
    def getValue (self):
        return self.value
    # Function to set the value of the node to variable v
    def setValue (self,v):
        self.value = v

# This is the class for the linked list
class List(object):
    # Intializer for the beginning of the list (root(r)) and the size of the list
    def __init__(self,r = None):
        self.root = r
        self.size = 0

    # Function to get the size of the list
    def getSize (self):
        return self.size

    # Function to add node to list
    def addNode(self, x):
        newNode = Node(x, self.root)
        if self.root: # If there is another node in the list
            self.root.setPrev(newNode)      # Assigning the root nodes previous node to the new node
        self.root = newNode
        self.size += 1

    #Function to remove node from list
    def removeNode (self, x):
        thisNode = self.root # getting current node to use for removal
        previousNode = None # getting previous node, for change of pointer
        while thisNode: #To iterate through the list
            if thisNode.getValue() == x:
                next = thisNode.getNext() # This is setting the next pointer
                prev = thisNode.getPrev() # This is setting the prev pointer

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

    """NEED TO FINISH!"""
    """def displayList(self):
        listedList = []
        x = self.value
        while x!=None:
            listedList.append(str(x.value))
            x = x.next
        print ("List: ",",".join(listedList))"""


linkedList = List()
linkedList.addNode(26)
linkedList.addNode(14)
linkedList.addNode(39)
linkedList.addNode(65)
linkedList.addNode(47)
print(linkedList.removeNode(45))
print(linkedList.removeNode(39))
#linkedList.displayList()




