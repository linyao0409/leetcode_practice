# 905_Sort_Array_By_Parity.py
"""Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

"""
#not fast enough
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenArr = [x for x in nums if x&1 == 0]
        oddArr = [x for x in nums if x&1 == 1]
        nums[:] = evenArr + oddArr
        return nums


#creating a list to store element from the head and tail by two index l(eft) r(ight)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        numsCopy = [0] * length
        l,r = 0,length-1
        for x in nums:
            if x&1 == 0:
                numsCopy[l] = x
                l += 1
            else:
                numsCopy[r] = x
                r -= 1
        return numsCopy


#without createing a new list but the relative order of emelments are break
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] %2 > nums[right]%2:
                nums[left],nums[right] = nums[right],nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] %2 == 1:
                right -= 1
        return nums
