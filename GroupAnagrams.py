'''
Leetcode Daily Challenge: Group Anagrams

author: @Clatyon Williams
Description:
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Result:
Runtime: 104 ms, faster than 52.01% of Python3 online submissions for Group Anagrams.
Memory Usage: 16.8 MB, less than 39.62% of Python3 online submissions for Group Anagrams.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if (len(strs) == 1):
        #    return strs
        sortedDict = {}
        for i in strs:
            key = ''.join(sorted(i))
            if (key in sortedDict.keys()):
                sortedDict[key].append(i)
            else:
                sortedDict[key] = []
                sortedDict[key].append(i)
        retList = []
        for key in sortedDict:
            retList.append(sortedDict[key])
        return retList
