#26_Remove_Duplicates_from_Sorted_Array.py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=0
        count =0 #count momory how many time the nums the same
        for x in nums[1:]: # start from the second element because the first element must overlap
            if x == nums[i]:
                count += 1
                continue
            else:
                i += 1
                nums[i] = x
        #for i in range(count):
        #nums.pop()
        return len(nums) - count

            
    
    
    