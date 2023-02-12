# 206. Reverse Linked List.py
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        current = head
        temp = current

        curNext = current.next

        while curNext:
            current = curNext
            curNext = current.next
            current.next = temp

            if temp == head:
                temp.next = None
            temp = current
        
        head = current
        return head

