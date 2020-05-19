"""
+++++++++++++++++++++++++++++++++++++

Leet Code
997. Square of a Sorted Array
Array practice

Solution is sub-optimal
+++++++++++++++++++++++++++++++++++++

https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

"""

import unittest

def sq_arr3(arr):
    """square all the values in a sorted array and return the values in 
    increasing order

    Runtime complexity: O(n)*2 (best solution on LeetCode is O(n)*1)
    Space complexity: O(n)*2

    Example:
    >>> sq_arr3([-1, 0, 3])
    [0, 1, 9]
    """

    # use the two pointer technique to sort the array
    i = 0 # index starts at the beginning of the list
    j = len(arr) - 1 # index starts at the end of the list

    squares = [] # create a new list to hold the squared values that are sorted

    while i <= j: # make sure the indexs don't overlap
        
        # add the largest value to the end of the list
        if arr[i]**2 >= arr[j]**2:
            squares.append(arr[i]**2) 
            i += 1
        
        elif arr[i]**2 < arr[j]**2:
            squares.append(arr[j]**2) 
            j -= 1

    squares.reverse()
    return squares


def sq_arr2(arr):
    """square all the values in a sorted array and return the values in 
    increasing order

    Runtime complexity: O(n^2) because of using .insert(0)
    Space copplexity: O(n^2) because of using .insert(0)"""

    # use the two pointer technique to sort the array
    i = 0 # index starts at the beginning of the list
    j = len(arr) - 1 # index starts at the end of the list

    squares = [] # create a new list to hold the squared values that are sorted

    while i <= j: # make sure the indexs don't overlap
        
        if arr[i]**2 <= arr[j]**2:
            squares.insert(0, arr[j]**2) # add the largest value to the end of the list
            j -= 1
        
        elif arr[i]**2 > arr[j]**2:
            squares.insert(0, arr[i]**2) 
            i += 1

    return squares


class testSq_Arr3(unittest.TestCase):
    """Test the sq_arr3 function."""

    def test_sq_arr3(self):

        test1 = [-1, 0, 3]
        test1_expected = [0, 1, 9]

        test2 = [-4, 0, 3]
        test2_expected = [0, 9, 16]

        test3 = [-10, -4, -3, 2]
        test3_expected = [4, 9, 16, 100]

        test4 = []
        test4_expected = []

        test5 = [5]
        test5_expected = [25]

        self.assertEqual(sq_arr3(test1), test1_expected)
        self.assertEqual(sq_arr3(test2), test2_expected)
        self.assertEqual(sq_arr3(test3), test3_expected)
        self.assertEqual(sq_arr3(test4), test4_expected)
        self.assertEqual(sq_arr3(test5), test5_expected)


if __name__ == '__main__':

    unittest.main()  
