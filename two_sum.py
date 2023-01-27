class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashTable = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in HashTable:
                return [HashTable[temp],i]
            HashTable[nums[i]] = i