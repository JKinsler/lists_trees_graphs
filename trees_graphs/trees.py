"""Practice creating a tree structure and solving related tree problems."""

import pdb

class Node():
    """Node for a tree class"""

    def __init__(self, data, children=None):

        self.data = data
        self.children = children or []

    def __repr__(self):
        return "<Node {}>".format(self.data)

    def find(self, data):
        """Return node object with this data"""

        # pdb.set_trace()
        to_visit = [self]

        while to_visit:
            #depth first search
            current = to_visit.pop()
            # print(f'current: {current}, current type: {type(current)}')
            # print(f'to_visit: {current}, to_visit type: {type(current)}')

            if current.data == data:
                return True

            else:
                to_visit.extend(current.children)

        return False


class Tree():
    """Tree class"""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return "<Tree root={}".format(self.root)

    def find_in_tree(self, node):
        """Find a node object in the tree

        Start at root. 
        Return none if not found."""
        # pdb.set_trace()
        return self.root.find(node.data)


if __name__ == '__main__':

    Clif = Node('Clif')
    Gar = Node('Gar')
    Omlet = Node('Omlet')
    Daf = Node('Daf')

    print(f'\n\nClif: {Clif}')
    print(f"Clif's children: {Clif.children}")

    print('\n\nAdding children to cliff')
    Clif.children.extend([Omlet, Gar, Daf])
    print(Clif)
    print(f"Clif's children: {Clif.children}")


    print("Is 'Omlet' Clif's child?")
    print(Clif.find('Omlet'))

    print(f'\n\nAdding children to Daf')
    Sam = Node('Sam')
    Pam = Node('Pam')
    Bam = Node('Bam')
    Daf.children.extend([Sam, Pam, Bam])
    print(f"Daf's children: {Daf.children}")

    print(f'\n\nAdding children to Omlet')
    Curly = Node('Curly')
    Puf = Node('Puf')
    Fluf = Node('Fluf')
    Omlet.children.extend([Curly, Puf, Fluf])
    print(f"Omlet's children: {Omlet.children}")

    print(f'\n\nCreating Clifs_tree as a tree class')
    clifs_tree = Tree(Clif)
    print(f'\n\nIs Fluf in clifs_tree?')
    print(clifs_tree.find_in_tree(Fluf))








