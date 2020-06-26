"""
practicing binary search tree

"""

class binaryNode():

    def __init__ (self, data, right = None, left = None):

        self.data = data
        self.right = right
        self.left = left

    def __repr__ (self):

        return '<binaryNode | data: {data}, left: {left}, right: {right}'.format(data = self.data, left = self.left, right = self.right)

    def insert_iter(self, data):
        """iterative method for adding a node to a binary search tree"""

        new_node = binaryNode(data)

        current = self # pointer for furthest most point searched in the tree
        last = None # trailing pointer for current

        # traverse to the endpoint of the tree
        while current:
            last = current
            if new_node.data < current.data:
                current = current.left

            elif new_node.data > current.data:  
                current = current.right

            else:
                break


        # insert the new node
        if new_node.data < last.data:
                last.left = new_node

        elif new_node.data > last.data:  
            last.right = new_node

        else:
            return None


    def insert_recur(self, data):
        """recursive method for adding a node to a binary search tree"""

        if data < self.data:
            if self.left is None:
                self.left =  binaryNode(data)
            else:
                self.left.insert_recur(data)

        elif data > self.data:
            if self.right is None:
                self.right = binaryNode(data)
            else:
                self.right.insert_recur(data)

        else:
            self.data = data


if __name__ == '__main__':

    root = binaryNode(10)

    root.insert_iter(5)
    root.insert_iter(15)
    root.insert_iter(8)
    root.insert_iter(12)

    print(root) # expect 10

    root2 = binaryNode(10)
    root2.insert_recur(5)
    root2.insert_recur(15)
    root2.insert_recur(8)
    root2.insert_recur(12)

    print(root2) # expect 10


