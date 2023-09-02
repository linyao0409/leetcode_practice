#215. Kth Largest Element in an Array.py
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 """

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        heap_min = [ -x for x in nums]

        heapq.heapify(heap_min)

        for i in range(k):
            a = heapq.heappop(heap_min)
        return -a