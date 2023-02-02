# 15. 3Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newNums = nums
        newLength = len(newNums)

        result = []

        for i in range(newLength):
            for j in range(i+1,newLength):
                for k in range(j+1,newLength):
                    if newNums[i] + newNums[j] + newNums[k] == 0:
                        temp =  sorted([newNums[i] , newNums[j] , newNums[k]])
                        if temp not in result:
                            result.append(temp)
        return result


        
        




