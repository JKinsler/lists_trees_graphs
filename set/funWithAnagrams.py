"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

HackerRank
Facebook screening test

Optimal solution
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Fun with Anagrams

Take in an array of strings. Return a sorted list of strings where anagrams that 
follow the first matching item is removed."""

import unittest

def funWithGrams3(arr):

    unique = set()

    for word in arr:
        bol = False
        for phr in unique:
            grams = is_gram(word, phr)
            if grams == True:
                bol = True
                break
        if bol == False:
            unique.add(word)

    new_list = list(unique)
    new_list.sort()

    return new_list


def is_gram(first, sec):
    """"check if two words are anagrams"""

    f_dict = {}
    for ltr in first:
        if ltr not in f_dict:
            f_dict[ltr] = 1
        else:
            f_dict[ltr] += 1

    s_dict = {}
    for ltr in sec:
        if ltr not in s_dict:
            s_dict[ltr] = 1
        else:
            s_dict[ltr] += 1

    if f_dict == s_dict:
        return True

    else: 
        return False


class TestGrams(unittest.TestCase):
    """unittest for funWithGrams3."""

    def test_funWithGrams3(self):

        arr1 = [] # edge case, empty list
        arr1_sol = [] # expected solution

        arr2 = ['ana'] # edge case, list length = 1
        arr2_sol = ['ana'] # expected solution

        arr3 = ['a', 'b', 'c', 'a', 'd'] # general case
        arr3_sol = ['a', 'b', 'c', 'd'] # expected solution

        arr4 = ['a', 'b', 'b', 'b', 'c', 'a', 'd'] # general case
        arr4_sol = ['a', 'b', 'c', 'd'] # expected solution

        arr5 = ['poke', 'pkoe', 'okpe', 'ekop'] # general case
        arr5_sol = ['poke'] # expected solution

        self.assertEqual(funWithGrams3(arr1), arr1_sol)
        self.assertEqual(funWithGrams3(arr2), arr2_sol)
        self.assertEqual(funWithGrams3(arr3), arr3_sol)
        self.assertEqual(funWithGrams3(arr4), arr4_sol)
        self.assertEqual(funWithGrams3(arr5), arr5_sol)


if __name__ == '__main__':

    unittest.main()

"""
solution:
Time complexity: O(n)
Space complexity: O(n)

is_gram
Time complexity: O(n)
Space complexity: O(1)

funWithGrams
Time complexity: O(n)
Space complexity: O(n)

"""

'''
NON WORKING CODE
def funWithAnagrams(text):
    
    for i, word in enumerate(text):
        # seen.append(i)
        for j, phr in enumerate(text):
            # if j not in seen:
            #     if word == phr:
            #         text.pop(j)
            #         j = j-1
                    # seen.remove(j)
            if j > i:
                grams = is_gram(word, phr)
                if grams == True:
                    text.pop(j)

    text.sort()

    return text

def funWithAnagrams2(text):
    """blah"""

    seen = []
    if len(text) > 0:
        for i, word in enumerate(text):
            seen.append(i)
            for j, phr in enumerate(text):
                if j not in seen:
                    grams = is_gram(word, phr)
                    if grams == True:
                        text.pop(j)
                        if i in seen:
                            seen.remove(i)

        text.sort()
    return text


def pop_equal(arr):
    """pops values that repeated in the same arr"""

    seen = []
    for i, word in enumerate(arr):
        seen.append(i)
        for j, phr in enumerate(arr):
            if j not in seen:
                if word == phr:
                    arr.pop(j)
                    j = j-1
                    seen.remove(i)
            # if j > i:
            #     if word == phr:
            #         arr.pop(j)

    return arr
'''
