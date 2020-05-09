"""
++++++++++++++++++++++++++++++++++
Cracking the coding interview 
p 90 problem 1.1
++++++++++++++++++++++++++++++++++

"""

import pdb

# as solved by JK
def is_unique(str):
    """Test whether the characters in a string are unique

    Runtime complexity: O(n^2)
    Storage complexity: O(n^2)
    """
    for i, ltr in enumerate(str):
        for j, char in enumerate(str):
            if i<j:
                if ltr == char:
                    return False
    return True

# #CCI solution
# # found on pg 192 of CCI
# def is_unique_2(str):
#     """CCI solution for whether characters in a string are unique"""

#     char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     if len(str) > 26:
#         return False

#     for letr in lower(str):

def is_unique_CCI(arr):
    """Test whether the characters in a string are unique.

    Runtime complexity: O(n)
    Storage complexity: O(n)
    """

    chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    
    if len(arr) > 26:
        return False


    else:
        if arr.islower() == False:
            arr = arr.lower()
        
        # pdb.set_trace()
        for ltr in arr:
            if ltr not in chars:
                return False
            else:
                chars.remove(ltr)
        return True


# def is_unique_alternate(arr):
#     """Test whether characters in a string are unique. 

#     This solution doesn't work because the set re-orders. 
#     Might be useful to use a dictionary that count letters instead."""

#     pdb.set_trace()
#     arr_list = list(arr)
#     arr_set = list(set(arr_list))

#     if arr_set == arr_list:
#         return True

#     else:
#         return False
