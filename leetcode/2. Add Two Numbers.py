"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr_ans = dummy
        p1,p2 = l1,l2
        move1 = False

        while p1 or p2:
            temp_sum = 0
            if p1 and p2:
                temp_sum = p1.val + p2.val
                p1 = p1.next
                p2 = p2.next
                temp_sum += int(move1)
                move1 = False
                if temp_sum >= 10:
                    temp_sum = temp_sum - 10
                    move1 = True
                ptr_ans.next = ListNode(temp_sum)
                ptr_ans = ptr_ans.next
            
            elif p1:
                temp_sum = p1.val 
                p1 = p1.next
                temp_sum += int(move1)
                move1 = False
                if temp_sum >= 10:
                    temp_sum -= 10
                    move1 = True
                ptr_ans.next = ListNode(temp_sum)
                ptr_ans = ptr_ans.next
            else: # if p2
                temp_sum = p2.val 
                p2 = p2.next
                temp_sum += int(move1)
                move1 = False
                if temp_sum >= 10:
                    temp_sum -= 10
                    move1 = True
                ptr_ans.next = ListNode(temp_sum)
                ptr_ans = ptr_ans.next
        if move1 == True:
            ptr_ans.next = ListNode(1)
        return dummy.next

