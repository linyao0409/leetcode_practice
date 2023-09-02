
"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 切半
# ＲＥＶＥＲＳＥ後一半
# ＭＥＲＧＥ ＴＨＥＭ
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head: Optional):
            if not head or not head.next:
                return head
            cur = head
            temp = head

            cur_next = cur.next
            while cur_next:
                cur = cur_next
                cur_next = cur_next.next

                if ( temp == head):
                    temp.next = None
                    cur.next = temp
                else:
                    cur.next = temp
                temp = cur
            return cur

        #if linklist is empty
        if head == None or (not head.next) or (not head.next.next):
            # empty , 1 element , 2 elements
            return head
        # make sure that ll at least contain 3 elements
        length = 1
        cur = head
        while cur.next:
            cur = cur.next 
            length += 1

        merge_time = length // 2
        pt2 = head
        p1_temp = head
        if length % 2 ==0: # even
            for i in range(length//2):
                pt2 = pt2.next
            for i in range(merge_time - 1):
                p1_temp = p1_temp.next
            
            
        else: # odd
            for i in range((length//2)+1):
                pt2 = pt2.next
            for i in range(merge_time):
                p1_temp = p1_temp.next
        
        p1_temp.next = None

        pt1 = head
        pt2 = reverse(pt2)

        pt1_id,pt2_id = pt1,pt2

        for i in range(merge_time):
            temp1 = pt1_id.next
            temp2 = pt2_id.next
            pt1_id.next = pt2_id
            pt2_id.next = temp1

            pt1_id = temp1
            pt2_id = temp2
        
        return head
        # reverse pt2
            

            
            


        """
        Do not return anything, modify head in-place instead.
        """