"""Practice writing the lined list class, node class and their associated 
methods."""

import pdb

class Node():
    """Creates a node"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node| data:{}, next:{}>"\
                        .format(self.data,
                                self.next.data if self.next else None,
                                )


class LinkedList():
    """creates a Linked List."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Adds a node to the linked list"""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


    def print(self):
        """Prints all the nodes in the linked list"""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find(self, info):
        """Search the linked list for 'info' that is given as an input parameter"""

        current = self.head

        while current is not None:
            if current.data == info:
                return True

            current = current.next

        return False

    def remove(self, info):
        """remove an item from a linked list"""

        current = self.head

        while current is not None:
            ahead = current.next
            if self.head.data == info:
                self.head = ahead
                return

            if ahead.data == info:
                current.next = ahead.next
                return

            current = current.next

    def rem_dupl(self):
        """remove duplicate nodes from a linked list."""

        # pdb.set_trace()
        cur = self.head
        
        if cur:
            words = set()
            words.add(self.head.data)

        while cur is not None:
            
            cur = cur.next

            if cur.next is None: 
                break

            elif cur.next.data not in words:
                words.add(cur.next.data)

            while cur.next.data in words:
                cur.next = cur.next.next


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.data])
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return ll




if __name__ == '__main__':

    """Tests to run when we call the function."""

    """Test linked list and node class functions
    print('\n\nCreate instance "test_node" of class Node')
    test_node = Node('first')
    print(f'test_node: {test_node}')
    print(f'test_node.data: {test_node.data}')
    print(f'test_node.next: {test_node.next}')

    print('\n\nCreate instance "my_ll" of class Linked List')
    my_ll = LinkedList()
    print(f'my_ll.head: {my_ll.head}')
    print(f'my_ll.tail: {my_ll.tail}')

    print('\n\nadding data to my_ll')
    my_ll.append('first')
    my_ll.append('second')
    my_ll.append('third')
    my_ll.append('fourth')
    print(f'my_ll.head.data: {my_ll.head.data}')
    print(f'my_ll.head.next: {my_ll.head.next}')
    print(f'my_ll.tail.data: {my_ll.tail.data}')

    print(f'\n\nprinting my_ll:')
    my_ll.print()

    print('\n\n"second" is in my_ll:')
    print(my_ll.find('second'))

    print('"fourth" is in my_ll:')
    print(my_ll.find('fourth'))

    print('removing "second" from my_ll')
    my_ll.remove('second')

    print(f'printing my_ll:')
    my_ll.print()

    print('\n\nremoving "first" from my_ll')
    my_ll.remove('first')

    print(f'printing my_ll:')
    my_ll.print()

    print('\n\nremoving "fourth" from my_ll')
    my_ll.remove('fourth')

    print(f'printing my_ll:')
    my_ll.print()

    print('\n\nremoving "third" from my_ll')
    my_ll.remove('third')

    print(f'printing my_ll:')
    my_ll.print()
    """

    """test CCI coding problems"""

    """test case a"""
    # print('\n\nCreate instance "CCI_21a_ll" of class Linked List')
    # CCI_21a_ll = LinkedList()
    # print(f'CCI_21a_ll.head: {CCI_21a_ll.head}')
    # print(f'CCI_21a_ll.tail: {CCI_21a_ll.tail}')

    # print('\n\nadding data to CCI_21a_ll')
    # CCI_21a_ll.append('a')
    # CCI_21a_ll.append('a')
    # # CCI_21a_ll.append('third')
    # # CCI_21a_ll.append('fourth')
    # print(f'CCI_21a_ll.head.data: {CCI_21a_ll.head.data}')
    # print(f'CCI_21a_ll.head.next: {CCI_21a_ll.head.next}')
    # print(f'CCI_21a_ll.tail.data: {CCI_21a_ll.tail.data}')

    # print(f'\n\nprinting CCI_21a_ll:')
    # CCI_21a_ll.print()

    # print(f'\n\nremove duplicates from CCI_21a_ll:')
    # CCI_21a_ll.rem_dupl()
    # CCI_21a_ll.print()

    # """test case b"""
    # print('\n\nCreate instance "CCI_21b_ll" of class Linked List')
    # CCI_21b_ll = LinkedList()
    # print(f'CCI_21b_ll.head: {CCI_21b_ll.head}')
    # print(f'CCI_21b_ll.tail: {CCI_21b_ll.tail}')

    # print(f'\n\n remove duplicates from CCI_21b_ll:')
    # CCI_21b_ll.rem_dupl()
    # CCI_21b_ll.print()

    # print('\n\nCreate instance "CCI_21c_ll" of class Linked List')
    # CCI_21c_ll = LinkedList()
    # print(f'CCI_21c_ll.head: {CCI_21c_ll.head}')
    # print(f'CCI_21c_ll.tail: {CCI_21c_ll.tail}')

    # """test case c"""
    # print('\n\nadding data to CCI_21c_ll')
    # CCI_21c_ll.append('a')
    # CCI_21c_ll.append('b')
    # CCI_21c_ll.append('b')
    # CCI_21c_ll.append('b')
    # CCI_21c_ll.append('c')
    # # CCI_21c_ll.append('third')
    # # CCI_21c_ll.append('fourth')
    # print(f'CCI_21c_ll.head.data: {CCI_21c_ll.head.data}')
    # print(f'CCI_21c_ll.head.next: {CCI_21c_ll.head.next}')
    # print(f'CCI_21c_ll.tail.data: {CCI_21c_ll.tail.data}')

    # print(f'\n\nprinting CCI_21c_ll:')
    # CCI_21c_ll.print()

    # print(f'\n\n remove duplicates from CCI_21c_ll:')
    # CCI_21c_ll.rem_dupl()
    # CCI_21c_ll.print()


    """CCI python solutions"""
    """test case d"""
    print('\n\nCreate instance "CCI_21d_ll" of class Linked List')
    CCI_21d_ll = LinkedList()
    print(f'CCI_21d_ll.head: {CCI_21d_ll.head}')
    print(f'CCI_21d_ll.tail: {CCI_21d_ll.tail}')

    print('\n\nadding data to CCI_21d_ll')
    CCI_21d_ll.append('a')
    CCI_21d_ll.append('a')
    # CCI_21d_ll.append('third')
    # CCI_21d_ll.append('fourth')
    print(f'CCI_21d_ll.head.data: {CCI_21d_ll.head.data}')
    print(f'CCI_21d_ll.head.next: {CCI_21d_ll.head.next}')
    print(f'CCI_21d_ll.tail.data: {CCI_21d_ll.tail.data}')

    print(f'\n\nprinting CCI_21d_ll:')
    CCI_21d_ll.print()

    print(f'\n\nremove duplicates from CCI_21d_ll:')
    remove_dups(CCI_21d_ll)
    CCI_21d_ll.print()    


    """test case e"""
    print('\n\nCreate instance "CCI_21e_ll" of class Linked List')
    CCI_21e_ll = LinkedList()
    print(f'CCI_21e_ll.head: {CCI_21e_ll.head}')
    print(f'CCI_21e_ll.tail: {CCI_21e_ll.tail}')

    print('\n\nadding data to CCI_21e_ll')
    CCI_21e_ll.append('a')
    CCI_21e_ll.append('b')
    CCI_21e_ll.append('b')
    CCI_21e_ll.append('b')
    CCI_21e_ll.append('c')
    # CCI_21e_ll.append('third')
    # CCI_21e_ll.append('fourth')
    print(f'CCI_21e_ll.head.data: {CCI_21e_ll.head.data}')
    print(f'CCI_21e_ll.head.next: {CCI_21e_ll.head.next}')
    print(f'CCI_21e_ll.tail.data: {CCI_21e_ll.tail.data}')

    print(f'\n\nprinting CCI_21e_ll:')
    CCI_21e_ll.print()

    print(f'\n\n remove duplicates from CCI_21e_ll:')
    remove_dups(CCI_21e_ll)
    CCI_21e_ll.print()