"""
+++++++++++++++++++++++++++++++++++++

HackerRank 
Interview prep kit
Warm up challenge

Optimal Solution
+++++++++++++++++++++++++++++++++++++

Sock Merchant
"""

def sockMerchant(n, ar):
    """
    Return the total number of pairs of socks. The socks will be matched by 
    their color.

    Inputs:
    n: total number of socks
    ar: list of the socks with values representing their colors
    
    Example: 
    >>> sockMerchant(3, [1, 2, 1])
    1

    >>> sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    """
    
    socks = {} # make a dictionary to store the sock pairs
    
    # examine each sock in input list and add it to the dictionary
    for sock in ar:
        if sock not in socks:
            socks[sock] = 1
        else:
            socks[sock] += 1

    pair_count = 0 # create a variable to count the number of pairs

    # examine how many sock paris are in the dictionary
    for sock in socks:
        pair_count += (socks[sock] // 2)
        
    return pair_count


if __name__ == '__main__':
    
    from doctest import testmod
    if testmod().failed == 0:
        print('Congratulations! All tests passed')
    else: 
        print('Your code has an error.')


"""
Time complexity: O(n)
Space complexity: O(1)?

"""