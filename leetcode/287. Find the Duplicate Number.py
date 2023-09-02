"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # contain n+1 ints
        # range(1,n)
        d = dict()
        length = len(nums)
        for i in range(length):
            temp = nums[i]
            if temp in d:
                return temp
            else:
                d[temp] = True
        return 0
