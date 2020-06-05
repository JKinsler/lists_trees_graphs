"""
++++++++++++++++++++++++++++++++++
Cracking the coding interview 
p 90 problem 1.4
++++++++++++++++++++++++++++++++++

Given a string, write a funciton to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words. You can ignore casing and non-letter characters.

"""

def palindrome(phr):

    """
    check whether a string is a permutation of a palindrome. White space and
    capital letters are ignored.

    Input: str, string
    Output: bolean

    # permutaitons of 'Tact Coa' are 'atco cta' etc.

    Examples:
    >>> palindrome('Tact Coa')
    True

    >>> palindrome('fact')
    False

    >>> palindrome(' ')
    True

    >>> palindrome('')
    True
    

    Developer notes:
    - Time to solve: 15-20min
    - Runtime complexity: O(n)
    - Space complexity: O(n)
    """


    phr = phr.lower() # convert all characters in phr argument to lower case

    counter = {} # create an empty disctionary

    # create a set of all letters
    letters = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    # add the count of each letter to the dictionary 'counter'
    for ltr in phr:
        if ltr in letters:
            if ltr not in counter:
                counter[ltr] = 1
            else:
                counter[ltr] +=1

    # check that all values in the dictionary 'counter' are even, ecepting one 
    # or zero values


    odds = 0 # save the number of odd values
    for item in counter:
        if counter[item] %2 != 0:
            odds += 1

    if odds <= 1:
        return True

    else:
        return False


if __name__ == '__main__':
    
    from doctest import testmod
    if testmod().failed == 0:
        print('all tests passed')
    else:
        print('tests failed')


