# -*- coding: utf-8 -*-
"""
Leetcode Daily Challenge
Created on Thu Apr  2  2020

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

@author: Clayton

Runtime: 24 ms, faster than 96.97% of Python3 online submissions for Happy Number.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Happy Number.
"""

class Solution:
    def isHappy(self, n: int) -> bool:                
      return self.happyHelper(n,{})
    def happyHelper(self,n,visited):
      if n == 1:
         return True
      if n in visited:
         return False
      visited[n]= 1
      n = str(n)
      m = 0
      for i in n:
        m += int(i)**2
      return self.happyHelper(m,visited) 
