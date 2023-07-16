"""Write a method in python as following :

def has_cycle(head:ListNode)->int:
To take the head node of a singly linked list as input and returns None if there does not exist a cycle, and the node's data at the start of the cycle, if a cycle is present, (You do not know the length of the list in advance.)

For example:

Input: 1->2->3->4->5->None
Output: None
Input: 1->2->3->4->5->6->7->8
                ^___________|
Output: 4
Hint: Floyd’s Cycle Detection Algorithm a.k.a. Tortoise and Hare Algorithm

The ListNode Class and other supporting methods are included and declared as:

class ListNode:
    def __init__(self, data:int):
        self.data = data
        self.next = None
    def __iter__(self):
        current = self
        while current is not None:
            yield current # suspend and output current ListNode object
            current = current.next
def init_list(seq:list)->ListNode:
    head = None
    for seq_idx,i in enumerate(seq):
        if head is None:
            head = ListNode(i)
            tail = head
        elif type(i) is int and i < 0:
            for idx,n in enumerate(head):
                if idx == seq_idx+i:
                    tail.next = n
                    break
        else:
            tail.next = ListNode(i)
            tail = tail.next
    return head
For example:

Test	Result
print(has_cycle(init_list([1,2,3,4,5])))
None
print(has_cycle(init_list([1,2,3,4,5,6,7,8,-5])))
4
"""
def has_cycle(head:ListNode)->int:
    if head == None or head.next == None:
        return None
    ptr1 = head.next
    if ptr1 == None:
        return None
    ptr2 = head.next.next
    if  ptr2 == None:
        return None
    while ptr1 != ptr2:
        if ptr2 == None or ptr2.next == None:
            return None
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
    # ptr1 & ptr2 's poisition is overlap in the cycle
    ptr3 = head
    while ptr3 != ptr1:
        ptr1 = ptr1.next
        ptr3 = ptr3.next 
    return ptr3.data


"""
Write a method in python as following :

def is_valid_sudoku(board:list)->bool:
Given a 2D list array board as input, check whether the 9x9 2D board representing a partially completed Sudoku is valid. Specifically, check that no row, column, or 3 x 3 2D subarray contains duplicates. Return True if Sudoku rules are followed, or return False.
A 0-value in the 2D array indicates that entry is blank; every other entry is in 1,…,9

Hint: magic formula for 3x3 subarray: [(i//3)*3+j//3][(i%3)*3+j%3]
For example:
Test	Result
print(is_valid_sudoku(
[[0, 0, 0, 0, 0, 0, 0, 8, 1],
 [9, 0, 0, 0, 7, 0, 3, 0, 0],
 [0, 0, 0, 9, 2, 4, 0, 6, 0],
 [0, 8, 5, 0, 0, 0, 0, 0, 0], 
 [7, 4, 0, 0, 3, 0, 0, 2, 6], 
 [0, 1, 0, 0, 0, 9, 7, 0, 0], 
 [0, 6, 0, 0, 0, 1, 0, 0, 3], 
 [3, 2, 0, 0, 8, 7, 0, 0, 0], 
 [8, 0, 0, 0, 5, 6, 2, 1, 4]]))
True
print(is_valid_sudoku(
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0], 
 [0, 0, 0, 0, 7, 0, 0, 0, 0], 
 [8, 0, 7, 0, 0, 0, 0, 0, 4], 
 [0, 0, 3, 0, 5, 4, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 3, 4, 0], 
 [0, 0, 8, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 4, 2, 0, 0, 6], 
 [0, 0, 0, 0, 0, 0, 0, 0, 3]]))
False
"""

def is_valid_sudoku(board:list)->bool:
    # chech the value in board is valid

    #check the rows are valid ( contain 1 to 9 )
    for i in range(9):
        row_set = set()
        for j in range(9):
            temp = board[i][j]
            if temp != 0 and temp in row_set:
                return False
            else:
                row_set.add(temp)
        row_set = set()  # empty the set
    # check the cols are valid (contain 1 to 9 )
    # similar with the rows -> inverse the index of i & j
    for i in range(9): # i is col
        col_set = set()
        for j in range(9): # j is row 
            temp = board[j][i]
            if temp != 0 and temp in col_set:
                return False
            else:
                col_set.add(temp)
        col_set = set()  # empty the set
    # check the little 9 blocks
    for R in range(3):
        for C in range(3):
            r = R * 3
            c = C * 3 
            little_block = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] != 0 and board[i][j] in little_block:
                        return False
                    else:
                        little_block.add(board[i][j])
                little_bolck = set()
    return True
# write a fn such that fill the matrix
