#977_Squares_of_a_Sorted_Array.py
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = map((lambda x:x*x,nums))
        nums.sort()
        return nums
        


class Solution:
    # using two index from the leftest and rightest 
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        copy_nums = [0]*len_nums # create a list and initialize all element as 0
        # you can adjust the emelent directly without keep appending item
        # avoid to keep adjusting the length of list
        l = 0
        r = len(nums) - 1
        index = r
        while (l <= r) :
            if abs(nums[l]) >= abs(nums[r]):
                copy_nums[index] = nums[l]*nums[l]
                l += 1
                index -= 1
            else:
                copy_nums[index] = nums[r]*nums[r]
                r -= 1
                index -= 1
        return copy_nums
