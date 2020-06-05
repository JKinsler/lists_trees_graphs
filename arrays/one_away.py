"""
++++++++++++++++++++++++++++++++++
Cracking the coding interview 
p 90 problem 1.5
++++++++++++++++++++++++++++++++++

There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check
if they are one edit (or zero edits) away.

"""

def one_away(str1, str2):
    """
    Example:
    >>> one_away('ple', 'pale')
    True

    >>> one_away('pale', 'bake')
    False
    
    >>> one_away('pale', 'ale')
    True

    >>> one_away('p', '')
    True

    Developer Notes: 
    - solved 6/5/20
    - completion time: 31 min
    - Time complexity: O(n), where n is the lenght of the longer string
    - Space complexity: O(1)
    Likely the best case solution
    """

    i = 0 # index pointer for str1
    j = 0 # index pointer for str2
    diff = 0 # cound the number of differences between str1 and str2

    while i < len(str1) and j < len(str2):
        # check for a difference
        if str1[i] != str2[j]:
            diff += 1
            
            # check insertion or removal
            if str1[i] == str2[j + 1]:
                j += 1
            elif str1[i+1] == str2[j]:
                i += 1
            
            # check substitution
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    #check insertion or removal
    if len(str1) > i + 1:
        diff += 1
    elif len(str2) > i+1:
        diff += 1

    #check total number of differences
    if diff > 1:
        return False
    else:
        return True


def one_away_CCI(str1, str2):

    """CCI solution2 for one away problem

    Example:
    >>> one_away_CCI('ple', 'pale')
    True

    >>> one_away_CCI('pale', 'bake')
    False
    
    >>> one_away_CCI('pale', 'ale')
    True

    >>> one_away_CCI('p', '')
    True

    Developer Notes:
    - This solution has the advantage of stopping after the length of the shorter
    stirng is reached. 
    - This soution has internal definitions which reduces the length of the 
    code and possibly makes it easier to maintain

    """

    # check that the difference in lenghts of the two strings is no more than 1
    if abs(len(str1) - len(str2)) > 1:
        return False

    # get the shorter length string
    shorter = str1
    longer = str2
    if len(str1) > len(str2):
        shorter = str2
        longer = str1

    # track whether a difference is found between the two strings
    found_diff = False
    # set an index for each string
    index1 = 0 # associated with the shorter string
    index2 = 0 # associated with the longer string

    while index2 < len(longer) and index1 < len(shorter):
        if shorter[index1] != longer[index2]:
            # ensure that this is the first difference found
            if found_diff:
                return False
            found_diff = True

            # on replace, move the shorter pointer
            if len(shorter) == len(longer): 
                index1 += 1
            
        # if matching, move the shorter pointer
        else:
            index1 += 1
        # always move the longer pointer
        index2 += 1 

    return True



if __name__ == '__main__':

    from doctest import testmod
    if testmod().failed == 0:
        print('all tests passed')
    else:
        print('your code has an error')

