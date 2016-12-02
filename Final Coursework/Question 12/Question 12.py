###QUESTION 12###

class Node(object):
    """The Class to hold and manage properties of a node"""
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def treeInsert(tree, item):
    """Function to insert nodes into the tree"""
    if tree == None:
        tree = Node(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=Node(item)
            else:
                treeInsert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=Node(item)
            else:
                treeInsert(tree.right,item)
    return tree

def postorder(tree):
    """Function to traverse the tree"""
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)

def inOrder(tree):
    """Function to order the tree iteratively"""
    currentNode = tree
    holder=[] # H
    complete = False
    while not complete:
        while currentNode:
            holder.append(currentNode)
            currentNode = currentNode.left # Display left node
        else:
            if(len(holder) >0 ): # If holder is empty
                    currentNode = holder.pop() # removing and returning last element from list
                    print (currentNode.value)
                    currentNode = currentNode.right # Display right node
            else:
                complete = True

if __name__ == '__main__':
  t=treeInsert(None,6);
  treeInsert(t,10)
  treeInsert(t,5)
  treeInsert(t,2)
  treeInsert(t,3)
  treeInsert(t,4)
  treeInsert(t,11)
  inOrder(t)

"""Description"""
"""With this question I was tasked with taking a given TREE_SORT algorithm which included an recursive
INORDER function. I had to re-implement the INORDER function iteratively.
"""

"""Big O Notation"""
"""The big o notation for this question is 0(n^2)"""
