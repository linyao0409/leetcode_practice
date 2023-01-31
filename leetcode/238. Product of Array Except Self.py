#238. Product of Array Except Self.py
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countOfZero = nums.count(0)
        copyNums = nums[:]
        for i in range(countOfZero):
            copyNums.remove(0)
        productOfNonZeroList= numpy.prod(copyNums)
        
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                if countOfZero >= 2:
                    nums[i] = 0
                else:
                    nums[i] = int(productOfNonZeroList)
            else:
                if countOfZero >= 1:
                    nums[i] = 0
                else: #without zero in the list
                    nums[i] = int(productOfNonZeroList / nums[i])
        return nums[:]



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        length = len(nums)
        res = [1] * length
        for i in range(length):
            res[i] *= prefix
            prefix *= nums[i]
        for i in range(length-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i] 
        
        return res


            

        

        
        
        
        
        



