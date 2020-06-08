"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
How to: Work at Google - Example Coding / Engineering Interview
https://www.youtube.com/watch?v=XKu_SEDAykw&t=18s
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Given an array and an integer value, return whether two numbers in the 
array add up to the integer value.

Assume that the values in the array are in ascending order.

Examples:

in: [1, 2, 3, 9], sum = 8  
out: False

in: [1, 2, 4, 4], sum = 8
out: True


Questions to ask:
Are all the number in the array integers? yes
Can a single index be used twice? No
Are all the numbers positive? No
What to return? Bolean? Indeces of Pair? Bolean

"""

import unittest

def is_sum_sorted(arr, total):
    """
    return whether two numbers in the array add to 'total'

    this problem assumes that the input array is sorted
    this solution is a two pointer method

    Developer notes: 
    Time to solve 15min (including writing test cases)
    Runtime complexity: O(n)
    Space complexity: O(1)
    """

    # create index for the beginning and end of the array
    i = 0
    j = len(arr)-1

    while i < j:
        if arr[i] + arr[j] == total: 
            return True
        else:
            if arr[i] + arr[j] < total:
                i += 1
            else:
                j -= 1
    return False


def is_sum_unsorted(arr, total):

    """
    return whether two numbers in the array add to 'total'

    the input array is not guaranteed to be sorted
    """

    """
    pseudo code:
    
    solution 1
    sort --> apply method
    runtime: O(nlog(n))

    solution 2
    loop through the whole array O(n^2)

    """
    arr2 = sorted(arr)
    is_sum = is_sum_sorted(arr)

    if is_sum == True:
        return True

    else:
        return False


def is_sum_unsorted2(arr, total):

    """
    return whether two numbers in the array add to 'total'

    the input array is not guaranteed to be sorted
    find a method that is faster than the 'sort' function.
    
    developer notes:
    - needed a hint to get to this solution
    - runtime complexity: O(n)
    - space complexity: O(n)
    """


    comps = set([])

    for item in arr:
        if item in comps:
            return True
        else:
            comps.add(total - item)

    return False 



class testIsSum(unittest.TestCase):
    """tets the is_sum_sorted and is_sum_unsorted2 function."""

    def test_is_sum_sorted(self):

        self.assertEqual(is_sum_sorted([1, 2], 3), True)
        self.assertEqual(is_sum_sorted([], 4), False)
        self.assertEqual(is_sum_sorted([1, 2, 3, 4, 4], 4), True)
        self.assertEqual(is_sum_sorted([1, 2, 3, 4, 9], 8), False)

    def test_is_sum_unsorted2(self):
        
        self.assertEqual(is_sum_unsorted2([1, 3], 4), True)
        self.assertEqual(is_sum_unsorted2([6, 3, 2], 8), True)
        self.assertEqual(is_sum_unsorted2([6, 3, 2], 10), False)



if __name__ == '__main__':

    unittest.main()
