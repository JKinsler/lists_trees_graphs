"""CCI problem 4.3, page 109

List of Depths: Given a binary tree, design an algorithm which creates a linked 
list of all the nodes at each depth."""

def list_of_depths(BiTree):

"""
return a linked list with all the nodes from each depth of the tree

Runtime: O(n^2), where n is the total number of nodes in the tree 
Storage: O(n)
"""
    q = [BiTree] # create a list of nodes to visit
    lls = []

    while len(q) > 0: # this will not add additional runtime because q is constanty being reduced
        ll = LinkedList() # create a new linked list

        for i in range(len(q)): # this will add O(n) runtime for each node in the tree
            cur = q.pop(0) # pop(0) is O(n) runtime 
            print(cur)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

            ll.append(cur)

        lls.append(ll)
        print(ll.head.data)

    return lls
    

class Node():

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.next = next

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):

        if self.head is None:
            self.head = node
            self.tail = node

        if self.tail is not None:
            self.tail.next = node

        self.tail = node


if __name__ == '__main__':
    
    # create a Binary Tree
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.left = b
    a.right = c

    # test the 'list_of_depths' function
    sol = list_of_depths(a)

    #expect
    #sol[0].head.data = 'a'
    #sol[1].head.data = 'b'


