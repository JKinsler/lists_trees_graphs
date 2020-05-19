"""
+++++++++++++++++++++++++++++++++++
Linked list problem
Technique practice: reverse a linked list

+++++++++++++++++++++++++++++++++++

reverse a linked list

Assumes that a Node class and a Linked List class is in place.

pseudo code:"""

import pdb # debugger

def reverse_ll(ll):

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
        new_ll.tail.next = ll.head
        new_ll.tail = new_ll.tail.next

    return new_ll


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


if __name__ == '__main__':

    # create a linked list 'A' with nodes 'a' --> 'b' --> 'c' --> 'd'
    A = LinkedList()

    print(f'LinkedList A: {A}')

    A.append('a')
    A.append('b')
    A.append('c')
    A.append('d')

    print('Nodes in LinkedList "A"')
    A.print()

    print('reverse LinkedList "A"')
    D = reverse_ll(A)
    D.print()