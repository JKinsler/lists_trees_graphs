

def list_of_depths(BiTree):

    q = [BiTree] # create a list of nodes to visit
    lls = []

    while len(q) > 0: 
        ll = LinkedList() # create a new linked list

        for i in range(len(q)):
            cur = q.pop(0)
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


