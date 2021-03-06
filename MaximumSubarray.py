'''
Leetcode Daily Challenge
Maximum Subarray

author @Clayton
Date: 2020.04.03

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.\

Results:
Runtime: 60 ms, faster than 94.34% of Python3 online submissions
for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions
for Maximum Subarray.
'''

# O(n) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
              
        max_so_far = nums[0] 
        curr_max = nums[0] 

        for i in range(1,len(nums)): 
            curr_max = max(nums[i], curr_max + nums[i]) 
            max_so_far = max(max_so_far,curr_max) 

        return max_so_far
