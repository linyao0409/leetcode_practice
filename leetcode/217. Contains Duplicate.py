# 217. Contains Duplicate.py
"""
 Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if len(nums) == len(s):
            return False
        else:
            return True
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        s = set()
        for x in s:
            if x in nums:
                return True
            else:
                s.add(x)
        return False