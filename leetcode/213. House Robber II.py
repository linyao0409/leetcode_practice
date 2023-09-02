# 213. House Robber II.py
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return None
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0],nums[1])
        elif length == 3:
            return max(nums[0],nums[1],nums[2])
        
        dp_0 = [0] * length # 0 - length-2
        dp_1 = [0] * length # 1 - length-1

        dp_0[0] = nums[0]
        dp_0[1] = max(nums[0],nums[1])
        dp_1[1] = nums[1]
        dp_1[2] = max(nums[1],nums[2])

        for i in range(2,length-1):
            dp_0[i] = max(nums[i]+dp_0[i-2],dp_0[i-1])

            dp_1[i+1] = max(nums[i+1]+dp_1[i-1],dp_1[i])

        return max(dp_0[length-2],dp_1[length-1])
            

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2


            


        
