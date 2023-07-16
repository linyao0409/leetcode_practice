#1
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for x in s:
            if x == ')':
                if len(l)!=0 and l[-1] == '(':
                    l.pop()
                else:
                    return False

            elif x == '}':
                if len(l)!=0 and l[-1] == '{':
                    l.pop()
                else:
                    return False

            elif x == ']':
                if len(l)!=0 and l[-1] == '[':
                    l.pop()
                else:
                    return False
            else:
                l.append(x)

        if len(l) == 0:
            return True

        

""" (3選2)Linked List: Add Two Linked Lists of Digits
● Given two linked lists representing two non-negative integers. The digits are
stored in reverse order, and each of their nodes contains a single digit. Add
the two numbers and return the sum as a linked list.
For example, 3->6->5->None + 9->8->4->None = 2->5->0->1->None
"""

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def search(self,key):
        L = self
        while L and L.data != key:
            L = L.next
        return L
    
    def rec_search(self,key):
        L = self
        if L.data == key:
            return L
        elif L.next == None:
            return None
        else:
            return L.next.rec_search(key)
    
    def insert_after(self,new_node):
        new_node.next = self.next
        self.next = new_node
    
    def delete_nextnode(self):
        if self.next:
            self.next = self.next.next

    def delete_thisnode(self):
        self.data = self.next.data
        self.next = self.next.next

    def print_LL(self):
        current = self
        while current:
            print(current.data,end=" ")
            current = current.next
L = [1,3,5,7,9]

l1 = [3,6,5]
l2 = [9,8,4]
head1,head2 = None,None
tail1,tail2 = head1,head2
for x in l1:
    if head1 is None:
        head1 = ListNode(x)
        tail1 = head1
    else:
        tail1.next = ListNode(x)
        tail1 = tail1.next
for x in l2:
    if head2 is None:
        head2 = ListNode(x)
        tail2 = head2
    else:
        tail2.next = ListNode(x)
        tail2 = tail2.next
head1.print_LL()
head2.print_LL()





## second question of the midterm 

def Q2(L1,L2):
    L3 = ListNode(1000) # how to improve it 
    pt1 = L1
    pt2 = L2
    pt3 = L3

    # keep push till both None
    temp_sum = 0
    add_1 = False
    while pt1 or pt2:
        
        temp_sum = pt1.data + pt2.data
        if add_1:
            temp_sum += 1

        if temp_sum >= 10:
            add_1 = True
            if pt3 is None:
                pt3 = ListNode(temp_sum % 10)
                print(pt3.data)
            else:
                pt3.next = ListNode(temp_sum % 10)
            pt3 = pt3.next
        else:
            if pt3 is None:
                pt3 = ListNode(temp_sum)
            print(pt3.data)
            pt3 = pt3.next
            add_1 = False
        
        if pt1:
            pt1 = pt1.next
        if pt2:
            pt2 = pt2.next
    if add_1:
        pt3.next = ListNode(1)
    return L3.next


Q2(head1,head2).print_LL()


# Q3 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length1 = len(s)
        length2 = len(t)

        if length1 != length2:
            return False

        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in t:
            if i not in d:
                return False
            else: 
                d[i] -= 1
                if d[i] == 0:
                    del d[i]

        return True


# Q3
"""
(3選2)Sort: Compute A Salary Threshold
● Given existing salaries and the target payroll. Design an algorithm for
computing the salary cap and return it; For example, if there were five employees with salaries last year were $90, $30, $100, $40, and $20, and the
target payroll this year is $210, then 60 is a suitable salary cap, since 60 + 30
+ 60 + 40 + 20 = 210.
"""

#3 
def salary_cap(L:list,target:int)->int:
    L.sort()
    total_sum = target
    length = len(L)
    for x in L:
        print(total_sum,length,total_sum/length)
        if x < total_sum /  length:
            total_sum -= x
            length -= 1
        else:
            return total_sum/length
#salary_cap([90,30,100,40,20],210)
#salary_cap([6,8,14],22)



    

    