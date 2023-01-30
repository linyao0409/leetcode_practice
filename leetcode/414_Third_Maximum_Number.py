# 414_Third_Maximum_Number.py
"""Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            for i in range(2):
                a.remove(max(s))
        return max(s)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        if len(l)<3:
            return max(l)
        else:
            return sorted(l)[-3]

