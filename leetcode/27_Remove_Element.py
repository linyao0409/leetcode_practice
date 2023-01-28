#27_Remove_Element.py
#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
