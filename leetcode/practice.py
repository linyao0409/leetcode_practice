
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        tempMax = 0
        ansMax = float('inf')

        if tempMax < 0:
            return tempMax
        else:
            for i in range(n):
                if tempMax + nums[i] > 0:
                    tempMax += nums[i]
                else:
                    tempMax = 0 
                
                if tempMax >= ansMax:
                    ansMax = tempMax
        return int(ansMax)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        new_list = None 
        current = head 

        while current != None:
            nextNode = current.next
            
            current.next = new_list
            new_list = current

            current = nextNode
        
        return new_list

