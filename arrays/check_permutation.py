"""
++++++++++++++++++++++++++++++++++
Cracking the coding interview 
p 90 problem 1.2
++++++++++++++++++++++++++++++++++

Given two strings, write a method to decide if one is a permutation of the other.

"""

def check_permutation(str1, str2):
    """check if the second string is a permutation of the first. 

    This solution assumes case and whitespace sensitivity.

    Input: 
        - str1, string e.g. 'dog'
        - str2, string e.g. 'god'
    Output: bolean, e.g. True 

    Examples: 
    >>> check_permutation('tao', 'oat')
    True
 
    >>> check_permutation('soap', 'idle')
    False

    >>> check_permutation('', 'a')
    False

    >>> check_permutation('a', 'a')
    True
    
    Developer comments:
    - problem solving time: 5min
    - runtime complexity = O(n) + O(m), because of converting the list to a set
    - space complexity = O(n) + O(m), because of converting the list to a set
    """

    if set(str1) == set(str2):
        return True
    else:
        return False


def check_perm(str1, str2):
    """check if the second string is a permutation of the first. 

    This solution assumes case and whitespace sensitivity.
    This solution excludes the use of a set.

    Input: 
        - str1, string e.g. 'dog'
        - str2, string e.g. 'god'
    Output: bolean, e.g. True 

    Examples: 
    >>> check_perm('tao', 'oat')
    True
 
    >>> check_perm('soap', 'idle')
    False

    >>> check_perm('', 'a')
    False

    >>> check_perm('a', 'a')
    True
    """

    if len(str1) != len(str2):
        return False

    first = "".join(sorted(str1))
    second = "".join(sorted(str2))

    if first == second:
        return True
    else:
        return False



    

if __name__ == '__main__':

    from doctest import testmod
    if testmod().failed == 0:
        print('all tests passed')
    else:
        print('there is an error in the code')