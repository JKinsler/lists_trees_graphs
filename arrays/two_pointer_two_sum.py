"""
+++++++++++++++++++++++++++++++++++++++++
Two sum array problem
Technique practice: two pointer solution

optimal solution
+++++++++++++++++++++++++++++++++++++++++

Given a sorted array of integers return whether the sum of any two integers in the list
is equal to 18.
"""
import unittest

def two_sum(arr):
    """Return whether two integers in the array sum to 18.

    Input: a sorted list of integers
    Outupt: Bolean True or False

    Examples: 
    >>> two_sum([3, 5, 6, 7, 12])
    True

    >>> two_sum([8, 10, 20])
    True
    
    >>> two_sum([1, 18])
    False

    >>> two_sum([-4, 6, 12, 20])
    True
    """

    # two pointer solution
    i = 0 # first index pointer
    j = len(arr) - 1 # second index pointer

    while i < j: # make sure the index's don't overlap
        if arr[i] + arr[j] == 18:
            return True

        elif arr[i] + arr[j] < 18: # since the array is sorted, increase i to increase the sum value
            i += 1

        elif arr[i] + arr[j] > 18: # since the array is sorted, decrease j to decrease the sum value
            j -= 1

    return False


class testTwoSum(unittest.TestCase):
    """unittest two_sum function"""

    def test_two_sum(self):

        arr1 = [] # edge case, an empty array, returns False
        arr2 = [1] # edge case, a single array, returns False
        arr3 = [-18, 5, 10, 11, 35] # standard input, returns False  
        arr4 = [-18, 5, 10, 13, 35] # standard input, returns True

        self.assertEqual(two_sum(arr1), False)
        self.assertEqual(two_sum(arr2), False)
        self.assertEqual(two_sum(arr3), False)
        self.assertEqual(two_sum(arr4), True)


if __name__ == '__main__':

    from doctest import testmod
    if testmod().failed == 0:
        print('Congratulations! All doc tests passed.')
    else: 
        print('test failure')

    unittest.main()


"""
Runtime complexity: O(n)
Storage complexity: O(1)
"""
