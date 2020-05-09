"""
+++++++++++++++++++++++++++++++++++++

HackerRank 
Interview prep kit
Warm up challenge

Optimal solution

+++++++++++++++++++++++++++++++++++++

Jumping on the clouds

Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0
"""


"""
Return:
- int, min number of jumps required

Input parameters:
- array comprised of binary integers, e.g. c = [0, 1 , 0, 0, 0, 1, 0]

Process:
- Can move from starting index to any other index that is +1 or +2
- Can move to indexs labeled '0'
- Must avoid indexs labeled '1'

Test case:
Input: c = [0, 1 , 0, 0, 0, 1, 0]
Return: 3
Comments: Take the path on indexes [0, 2, 4, 6], the starting index is not counted 
in the solution

"""

def jumpingOnClouds(c):
    """Return the minimum number of jumps possible."""

    # create list to track positions visited
    # visited = []
    # create variable to track number of visits
    visits = 0

    # create pointers for the list
    p = 0 # current index position
    p_n = p + 1 # nearest next index position available to visit
    p_n_n = p + 2 # furthest index position available to visit

    while p_n_n < len(c):
        if c[p_n_n] == 0:
            p = p_n_n
            
            # visited.append(p)
            visits += 1

        else:
            p = p_n
            
            # visited.append(p)
            visits += 1

        p_n = p + 1
        p_n_n = p + 2

    if p < len(c) - 1:
        p = p_n
        # visited.append(p)
        visits += 1

    return visits



if __name__ == '__main__':

    #jumpingOnClouds([])
    print(jumpingOnClouds([0])) # expect (1, [0])
    print(jumpingOnClouds([0, 1 , 0, 0, 0, 1, 0])) # expect (3, [2, 4, 6])

"""
Time complexity: O(n)
Space complexity: O(1) = constant space
    fixed not extra space

"""
