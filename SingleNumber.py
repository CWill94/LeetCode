# -*- coding: utf-8 -*-
"""
Leetcode Daily Challenge
Created on Wed Apr  1 17:01:42 2020

@author: Clayton
Single Number
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
Runtime: 84 ms, faster than 85.38% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 6.56% of Python3 online submissions for Single Number.
"""
#solution 1 runtime is 84ms and memory is 16.3mb
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums)== 1): return nums[0]
        try:
            for index,num in enumerate(nums):
                if(num == nums[index-1]):pass
                elif(num != nums[index+1]): return num
        except:
            return num