#283_Move_Zeroes_Move_Zeroes.py
"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

"""
Do not return anything, modify nums in-place instead.
"""
# too slow  
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        count = 0
        for x in nums:
            if x == 0:
                count += 1
        for i in range(count):
            nums.append(0)
            nums.remove(0)


#using two index i run faster j run slower to chach the nonzero value
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] == 0:
                continue
            else:
                nums[j] = nums[i]
                j += 1
        #fill 0 from j'th position
        for i in range(j,n):
            nums[i] = 0




class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        list of zero index
        pop zero index
        insert zero index in tail
        """

        #non_zeros = [i for i in range(len(nums)) if nums[i] <> 0]
        #zeros = [i for i in range(len(nums)) if nums[i] == 0]
        #using list comprehension
        non_zeros = [i for i in nums if i != 0]
        zeros = [i for i in nums if i == 0]

        zeros_to_insert = [0] * len(zeros)

        nums[:] = non_zeros + zeros_to_insert
