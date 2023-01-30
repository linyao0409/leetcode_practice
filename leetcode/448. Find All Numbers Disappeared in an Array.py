# 448. Find All Numbers Disappeared in an Array.py
"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 """

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        result = []
        for i in range(1,n+1):
            if i not in s:
                result.append(i)
        return result

"""Python3
Runtime
329 ms
Beats
97.49%
Memory
24.8 MB
Beats
30.94%
Click to check the distribution chart"""