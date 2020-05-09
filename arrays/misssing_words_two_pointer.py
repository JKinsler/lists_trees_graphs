"""

+++++++++++++++++++++++++++++++++++++++++
HackerRank
Missing Words
Twilio Prep Test problem

Optimal Solution
++++++++++++++++++++++++++++++++++++++++

Missing Words
A two pointer problem

Given two strings, one is a subsequence if all of the elements of the first string 
occur in the same order within the second string. They do not have to be contiguous
in the second string, but order must be maintained. For example, given the string 
'I like cheese', the words ('I', 'cheese') are one possible subsequence of that 
string. Words are space delimited. 

Given two strings, s and t, where t is a subsequence of s, report the words of s, 
missing in t (case sensitive), in the order they are missing.

Example:
s = 'I like cheese'
t = 'like'
"""

def missingWords4(s, t):
    """return the missing words from a string using a 2 pointer technique.

    Example:
    >>> missingWords4('I like cheese', 'like')
    'I cheese'

    >>> missingWords4('I am using HackerRank to improve programming', 'am HackerRank to improve')
    'I using programming'

    """

    new_s = s.split()
    # print(f'new_s: {new_s}')
    new_t = t.split()
    missing = []
    
    # designate two pointers
    s_index = 0 
    t_index = 0

    while s_index < len(new_s) and t_index < len(new_t):
        if new_s[s_index] != new_t[t_index]:
            missing.append(new_s[s_index])
            s_index += 1
            

        else:
            s_index += 1
            t_index += 1

    if s_index <= len(new_s):
        missing.extend(new_s[(s_index):])

    return(missing)



'''These solutions don't work

def missingWords(s, t):

    """
    this solution does not work for all test cases. 

    inputs:
    s = string
    t = string
    """
    missingWords = []
    
    new_t = t.split()
    new_s = s.split()

    for index, word in enumerate(new_s):
        if new_t[index] != word:
            missingWords.append(word)
            new_t[index] = word

    new_list = new_s - new_t

    return new_list


def missingWords2(s, t):
    """
    this solution does not work for all test cases. 

    inputs:
    s = string
    t = string

    output: 
    return
    each
    word

    This solution doesn't work if a word is repeated later but initially doesn't 
    have the right order of a missing word.
    """
    # missingWords = []
    
    new_s = s.split()
    # print(new_s)

    new_t = t.split()
    # print(new_t)

    missing = []

    while len(new_t) > 0:
        for word in new_s:
            if word not in new_t:
                missing.append(word)
            else:
                new_t.remove(word)

    return missing


def missingWords3(s, t):
    """
    this solution does not work for all test cases.
    
    inputs:
    s = string
    t = string

    output: 
    return
    each
    word
    """
    # missingWords = []
    
    new_s = s.split()
    new_t = t.split()
    missing = []
    j = 0

    for i in range(len(new_s)):
        if j <= len(new_t) - 1:
            if new_s[i] != new_t[j]:
                missing.append(new_s[i])
            else:
                j += 1

    return missing
'''



if __name__ == '__main__':
    
    s = 'I like cheese'
    t = 'like'
    print('Test1')
    print(missingWords4(s, t))

    # s = 'I am using HackerRank to improve programming'
    # t = 'am HackerRank to improve'
    # print('Test 2')
    # print(missingWords4(s, t))

    # first = 'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing'
    # second = 'Python is an easy to learn powerful programming language'
    # print('Test 3')
    # print(missingWords4(first, second))



    

