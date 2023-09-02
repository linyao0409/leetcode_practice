"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        l = [List[i] for i in range(length)]
        dummy = ListNode()
        ptr = dummy

        d = {}
        for i in range(length):
            if l[i]:
                d[i] = l[i].val
            else:
                d[i] = None
        sorted_val = sorted(d.items(), key=lambda x: x[1] if x[1] is not None else float('inf'))

        # min_index 
        # min_value
        # if one element in l is not None
        if l.count(None) < length: 
            i,x = sorted_val[0]
            l[i] = l[i].next
            new_x = l[i].val
            
            ptr.next = ListNode(x)
            ptr = ptr.next

            # Remove
            sorted_val.pop(0)
            # append
            sorted_val.append((i,new_x))
            sorted_val.sort(key = lambda item: item[1] if item[1] is not None else float("inf"))

        return dummy.next 

            