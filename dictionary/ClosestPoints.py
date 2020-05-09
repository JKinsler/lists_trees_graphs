"""
++++++++++++++++++++++++++++++++++
LeetCode
973.K Closest Points to Origin

Pseudo code only
++++++++++++++++++++++++++++++++++

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
"""

"""
Pseudo code:

Create a funciton that can take multiple inputs
Determine the distance of each point to the origin (a2 + b2 = c2) ==> sqrt(a2 + b2) is distance
Save distance in list of dictionaries with key = distance, value pairs = points
Sort the list of dictionaries (bubble sort)
put first k value pairs in a list
return the list

def close_pts(points, args, k):
    '''determine the k closes points'''


"""