#Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOf_i = 0
        for i in range(len(nums)):
            if count == 0:
                if nums[i] == 1:
                    count = 1
                else:
                    pass
            else:
                if nums[i] == 1:
                    count += 1
                else:
                    count = 0
            if count > maxOf_i:
                maxOf_i = count
        return maxOf_i        


Solution.findMaxConsecutiveOnes([1,0,1,1,1])

            