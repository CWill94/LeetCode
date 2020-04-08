'''
Leetcode Daily Challenge: Counting Elements
author: @Clatyon Williams

Description:

Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
Example 3:

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
Example 4:

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.

Result:
35 / 35 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 14.1 MB
Accepted Solutions Runtime Distribution
Sorry. We do not have enough accepted submissions to show distribution chart.

Accepted Solutions Memory Distribution
Sorry. We do not have enough accepted submissions to show distribution chart.
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        d,total = {}, 0
        for i in arr:
                d[i] =1
        for ints in arr:
            if(ints+1 in d):
                total +=1
        return total
