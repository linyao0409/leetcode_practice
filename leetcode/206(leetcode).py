# 206. Reverse Linked List.py
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:#判斷head是不是指向None 且判斷linklisted是不是擁有不只一個元素
            return head
        current = head
        temp = current # current,temp都指向head

        curNext = current.next #讓curNext先跑一格

        while curNext: #當curNext is not None into the loop
            current = curNext # current 跟上 curNext
            curNext = current.next #curNext 往右
            current.next = temp #reverse it(讓current指向左邊的temp)

            if temp == head: #第一格時候temp位置在最左邊（等於head) 讓temp指向None
                temp.next = None
            temp = current
        
        head = current # curNext == None 跳出while ，current 是最後一個元素 更新head位置
        return head

