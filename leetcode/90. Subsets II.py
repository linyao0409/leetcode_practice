# 90. Subsets II.py
"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)

        res = []
        subset = []
        def dfs(index):
            if len(subset) == length:
                res.append(subset.copy())
                return 
            
            subset.append(nums[index])
            dfs(index+1)
            subset.pop()
            while index < length and nums[i] == nums[i+1]:
                i = i+1
            dfs(index+1)
        dfs(nums)
        return res