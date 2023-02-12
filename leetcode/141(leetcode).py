#141. Linked List Cycle
"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:#imply no loop
            return False
        index1 = head.next 
        index2 = head.next.next

        while(index1 != index2): # 當index1不等於index2就繼續跑 如果等於＝有loop return True
            if(index2 == None or index2.next == None): # 如果index2== None or index2.next == None 代表index2可以跑到尾巴 so no loop , return False
                return False
            index1 = index1.next #移動一格
            index2 = index2.next.next # 移動兩格
        return True