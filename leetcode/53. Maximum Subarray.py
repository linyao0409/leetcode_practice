# 53. Maximum Subarray.py

""" Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempMax = 0
        ansMax = float("-inf")
        #leftIndex,rightIndex = 0, 0
        n = len(nums)
        maxNums = max(nums)
        if maxNums < 0:
            return int(maxNums)
        else:
            for i in range(n):
                if tempMax + nums[i] > 0:
                    #rightIndex = i
                    tempMax += nums[i]
                else:
                    tempMax = 0
                if tempMax >ansMax:
                    ansMax = tempMax
        return int(ansMax)
        
       