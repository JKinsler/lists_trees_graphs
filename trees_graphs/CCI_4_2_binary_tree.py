"""CCI problem 4.2

Minimal Tree: Given a sorted (increasing order) array with unique integer elements
write an algorithm to create a binary search tree with minimal height."""

class BinaryNode():
    """class for a binary search node"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def insert(self, value):
        """inserts new values into the binary tree."""


        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryNode(value)

        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinaryNode(value)

        else:
            self.data = self.data


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


"""My solution is not optimized for tree height"""
def mid(arr):
    """Finds the mid point in an array and return it

    Solution by JK"""

    
    arr_ln = len(arr)
    mid = arr_ln//2
    val = arr.pop(mid)

    return arr, val


def make_tree(arr):
    """Make a binary tree from a sorted integer array.

    Returns a binary tree"""

    for i in range(len(arr)):
        arr, val = mid(arr)

        if i == 0: 
            binary = BinaryNode(val)

        else:
            binary.insert(val)

    return binary
"""END JK solution"""


"""The CCI solution is optimized for tree height."""
def min_height(srt_arr):
    """CCI solution for problem 4.2 in Python"""

    # Leave the recursive loop if the srt_arr is empty 
    if len(srt_arr) == 0:
        return None
    
    # find the center of the array
    else: 
        mid = len(srt_arr)//2 
        
        # set the center point in the middle or first middle node of the array
        center = srt_arr[mid]

        #create a new BinaryTree from the center point
        tree = BinaryNode(center)
        
        # recurse on the left side of the array
        tree.left = min_height(srt_arr[:(mid)])

        # recurse on the right side of the array
        tree.right = min_height(srt_arr[(mid+1):])

        return tree
"""END CCI solution"""


if __name__ == '__main__':

    """# check that class and insert method are working.
    node_test = BinaryNode(10)
    node_test.insert(5)
    node_test.insert(3)
    node_test.insert(8)

    node_test.print_bi_tree()
    """

    """# test the 'mid' funciton
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    print(f'\n\narray: {arr}')

    print(f'array pop order: ')
    for val in range(len(arr)):
        print(mid(arr))
    """

    """# test my solution"""
    # print(f'test make_tree:')
    # tree = make_tree(arr_2)
    # print(tree)
    # tree.print_bi_tree()

    # test the CCI solution
    arr_2 = [10, 20, 30, 40, 50, 60, 70, 80]
    print(f'arr_2: {arr_2}')
    binary_tree = min_height(arr_2)
    print(f'binary_tree from arr_2:')
    binary_tree.print_bi_tree()








