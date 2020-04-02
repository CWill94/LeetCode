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
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        try:
            if(len(nums)== 1): return nums[0]
            for index,num in enumerate(nums):
                if(index == 0 or index == len(nums)-1):
                    if(num == nums[index-1]):pass
                    elif(num != nums[index+1]): return num
        except:
            return num

print(singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]))