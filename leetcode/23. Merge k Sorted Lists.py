"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
class Solution: 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        dummy = ListNode()
        ptr = dummy

        d = {}
        for i in range(length):
            if lists[i]:
                d[i] = lists[i].val
            else:
                d[i] = None
        sorted_val = sorted(d.items(), key=lambda x: x[1] if x[1] is not None else float('inf'))

        while lists.count(None) < length:
            i, x = sorted_val[0]
            lists[i] = lists[i].next
            new_x = lists[i].val if lists[i] else None

            ptr.next = ListNode(x)
            ptr = ptr.next

            sorted_val.pop(0)
            sorted_val.append((i, new_x))
            sorted_val.sort(key=lambda item: item[1] if item[1] is not None else float("inf"))

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, head: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Creating a list from the given LinkNode
        new=[]
        for i in head:
            while(i):
                new.append(i.val)
                i = i.next

        # Sort the list and reverse it
        a=sorted(new,reverse=True)
    
        # Create a ListNode from list
        """
        遍历排序后的列表a，对其中的每个元素i执行以下操作：

        创建一个新的节点ListNode(i, final)，该节点的值为i，下一个指针指向final。
        将final更新为新创建的节点，以便在下一次迭代时，新的节点将成为下一个要添加的节点的下一个节点。
        """
        final=None
        for i in a:
            final=ListNode(i,final)
        return final