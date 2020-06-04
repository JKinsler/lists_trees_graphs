"""
+++++++++++++++++++++++++++++++++++
Linked list problem
Technique practice: reverse a linked list

This solution works, but it is a brute force method. The run time is long. 
The solution should be simplified amd made faster. 
+++++++++++++++++++++++++++++++++++

Problem statement: reverse a linked list

Assumes that a Node class and a Linked List class is in place.

Time and space efficient solution can be found here: https://www.geeksforgeeks.org/reverse-a-linked-list/

"""

import pdb # debugger
import unittest



"""a = LinkedListNode('a')
b = LinkedListNode('b')
c = LinkedListNode('c')

A = LinkedList(a)
A.append(b)"""


def reverse_ll(ll):
    """Reverse a linked list

    For example:
    A = 'a' --> 'b' --> 'c'
    > reverse_ll(A)
    C
    C = 'c' --> 'b' --> 'a'
    
    Runtime complexity: (O)n^(n) approximate
    """

    # pdb.set_trace()
    # create a new, empty linked list
    new_ll  = LinkedList()

    # create a variable to track the current node
    if ll.head:
        current = ll.head

    # move through ll 
        while ll.head.next is not None:

            # find the node before the tail
            if current.next.next is None: 

            # add the tail to new_ll
                
                if new_ll.head is not None: # create the first node in the new_ll
                    new_ll.tail.next = current.next
                    new_ll.tail = new_ll.tail.next

                else: # create the first node in the new_ll            
                   new_ll.head = current.next # use current instead of current.data because current is already a node
                   new_ll.tail = current.next 

                # remove the value from the original linked list
                current.next = None

            # move through the linked list
            if current.next is None:
                if ll.head.next is None: 
                    break
                else:
                    current = ll.head

            while current.next.next is not None:
                current = current.next

    # add the final node to the new_ll
    if ll.head:
        if new_ll.head is not None: # added for addressing Linked Lists with a single node.
            new_ll.tail.next = ll.head
            new_ll.tail = new_ll.tail.next

        else:
            new_ll.head = ll.tail
            new_ll.head.next = None
            new_ll.tail = new_ll.head


    return new_ll

# runtime for this solution is very poor: O(n^2)
# # see alternative solutions for making this code faster


# RECOMMENDED SOLUTIONS ++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def reverse_ll_efficient(ll):
#     """Reverse a linked list."""

#     #initiate pointers
#     first = ll.head
#     node = ll.head
#     second = node.next


#     # flip the direction of the pointers
#     while first:

#         #add node
#         second.next = node
#         node.next = None

#         #increment first
#         first = first.next
#         node = first


#     # move the head to the front of the linked list
#     ll.head = second

#     return ll

# recursive method
# def reverse_ll_recurse(ll):      
#     """
#     :type head: ListNode         
#     :rtype: ListNode         
#     """         
          
#     if not ll.head or not ll.head.next: # when node is none             
#         return ll.head         
#     p = ll.reverse2(head.next) #        
#     ll.head.next.next = head #          
#     ll.head.next = None #          
#     return p

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CODE TO WRITE TEST CASES

class Node():
    """Node class for a linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node | data:{}, next:{}>".format(self.data, self.next.data 
                                                    if self.next.data else None)


class LinkedList():
    """Linked List class."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "<LinkedList | head: {}, tail: {}".format(self.head.data \
                                                        if self.head else None,
                                                        self.tail.data \
                                                        if self.tail else None,
                                                        )

    def append(self, data):
        """adds a Node to a Linked List class."""

        new_node = Node(data)

        if self.head is not None:
            self.tail.next = new_node

        else:
            self.head = new_node

        self.tail = new_node

    def print(self):
        """prints a linked list"""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


class TestReverseLL(unittest.TestCase):
    """Test the reverse_ll function."""

    def setUp(self):
        """set up before each test case"""
        
        # create a linked list 'A' with nodes 'a' --> 'b' --> 'c' --> 'd'
        self.A = LinkedList()
        self.A.append('a')
        self.A.append('b')
        self.A.append('c')
        self.A.append('d')

        # create a linked list 'Empty' with no nodes
        self.Empty = LinkedList()

        # create a linked list 'Single' with one node
        self.Single = LinkedList()
        self.Single.append('one')


    def test_reverse_ll_A(self):
        """test case for reversing Linked List A."""

        # reverse linked list A
        new_ll = reverse_ll(self.A)

        self.assertEqual(self.A.tail.data, new_ll.head.data)
        self.assertEqual(self.A.head.data, new_ll.tail.data)


    def test_reverse_ll_Empty(self):
        """test case for reversing Empty Linked List."""

        new_ll = reverse_ll(self.Empty)

        self.assertEqual(self.Empty.tail, new_ll.head)
        self.assertEqual(self.Empty.head, new_ll.tail)


    def test_reverse_ll_Single(self):
        """test case for reversing Single Linked List."""

        new_ll = reverse_ll(self.Single)

        self.assertEqual(self.Single.tail.data, new_ll.head.data)
        self.assertEqual(self.Single.head.data, new_ll.tail.data)


if __name__ == '__main__':

    # unittest.main()

    # create nodes


    # create linked list
    A = LinkedList()
    A.append('a')
    A.append('b')
    A.append('c')

