"""CCI problem 4.1 page 109"""
import unittest

class GraphNode():
    """Node for a graph"""

    def __init__(self, data, children = None):
        self.data = data
        self.children = children or []

    def __repr__(self):
        """helpful print format"""
        return "<GraphNode | {data} >".format(data = self.data)

def connected(first, second):
    """determine whether a first node is connected to a second node in a graph.

    Returns True or False"""

    to_see = [first]
    seen = []

    while len(to_see) > 0:
        current = to_see.pop(0)
        if current == second:
            return True
        else:
            seen.append(current)
            for child in current.children:
                if child not in seen:
                    to_see.append(child)
    return False

class Test (unittest.TestCase):
    def test_connected(self):
        south = GraphNode('south')
        north = GraphNode('north')
        east = GraphNode('east')
        south.children.extend([north, east])
        north.children.extend([east])
        print(south.children)

        self.assertEqual(connected(south, east), True)
        self.assertEqual(connected(north, south), False)
        self.assertEqual(connected(north, east), True)
        self.assertEqual(connected(east, south), False)



if __name__ == '__main__':

    # """create graph for test"""
    # print('creating graph "south":')
    # south = GraphNode('south')
    # print(south)

    # print('adding nodes "north", "east":')
    # north = GraphNode('north')
    # east = GraphNode('east')

    # south.children.extend([north, east])
    # north.children.extend([east])

    # print(f'south.children: {south.children}')
    # print(f'north.children: {north.children}')

    # print(f'test_1: is "south" connected to "east"?')
    # test_1 = connected(south, east)
    # print(test_1)

    unittest.main()