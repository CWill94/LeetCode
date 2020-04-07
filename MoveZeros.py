'''
LeetCode Daily Challenge: Move Zeros

author: @Clayton Williams
Date: 2020.04.04
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Result:
Runtime: 52 ms, faster than 44.22% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3
online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[count] = nums[i]
                count += 1
        while count < len(nums):
            nums[count] = 0
            count += 1
