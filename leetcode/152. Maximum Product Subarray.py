# 152. Maximum Product Subarray.py
"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = 1
        minimum = 1
        res = nums[0]

        for x in nums:
            if x == 0:
                res = max(res,0)
                maximum = 1
                minimum = 1
                continue
            temp = maximum * x
            maximum = max(maximum*x,minimum*x,x)
            minimum = min(minimum*x,temp,x)
            res = max(res,maximum)
        return res
            

