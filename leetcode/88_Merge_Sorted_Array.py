#88_Merge_Sorted_Array.py
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            pass
        else:
            for i in range(n):
                nums1[m+i]  = nums2[i]
            nums1.sort()

#clear way
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort() # using sort time complexithy is nlogn


# the fast way without using sort()
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m-1
        ptr2 = n-1
        ptr3 = m+n-1

        for i in range(n+m-1,-1,-1): # revise nums1 from tail without affecting the value we want to compare
            if ptr2 < 0:
                break
            
            if ptr1 >= 0 and nums1[ptr1] >= nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
