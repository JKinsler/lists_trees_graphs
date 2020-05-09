"""Practice with binary search trees"""

class BinaryNode():
    """A node for a Binary Tree."""

    def __init__(self, data, right=None, left=None):
        self.data = data
        # each node can only have two children: right, left
        self.right = right #right child
        self.left = left #left child


    def __repr__(self):
        """helpful print format."""

        return "<Binary Tree | data: {data}>".format(data = self.data)

    def insert(self, data):
        """Add a new node to a binary tree.

        Recursive method"""

        if data < self.data:
            if self.left is None:
                self.left = BinaryNode(data)

            else: 
                self.left.insert(data)

        elif data > self.data:
            if self.right is None:
                self.right = BinaryNode(data)

            else:
                self.right.insert(data)

        else:
            self.data = data

    def print_recursive(self):
        """print binary tree in order of left to right.

        Recursive method"""
        if self.left:
            self.left.print_recursive()
        
        if self.right:
            self.right.print_recursive()

        print(self.data)

    def print_bi_tree(self):
        """print binary tree using breath first tree method.
        Prints by level (breath first)
        Prints left to right in each level."""

        to_print = [self]
        # current = None

        while to_print:
            current = to_print.pop(0)
            if current:
                print(f'\t{current.data}')
                to_print.append(current.left)
                to_print.append(current.right)


        

    def find(self, value):
        """find value (given as an input parameter) in a binary tree

        Returns True or False."""

        current = self

        while current:
            if value == current.data:
                return True

            elif value < current.data:
                current = current.left

            elif value > current.data:
                current = current.right

        return False




if __name__ == '__main__':

    print(f'create "binary" as a node in a Binary Tree')
    binary = BinaryNode(50)
    print(f'binary: {binary}')

    print(f'insert node 40')
    binary.insert(40)

    print(f'\n\nadding and inserting nodes 60, 35, 45, 55, 65')

    binary.insert(60)
    binary.insert(35)
    binary.insert(45)
    binary.insert(55)
    binary.insert(65)
    print(f'\n\nprint_recursive for "binary"')
    binary.print_recursive()

    print(f'\n\nprint_bi_tree for "binary"')
    binary.print_bi_tree()

    print(f'\n\nIs "20" in binary?')
    print(binary.find(20))
    print(f'Is "65" in binary?')
    print(binary.find(65))