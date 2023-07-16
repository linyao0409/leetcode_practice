
def selection_sort(L): 
    length = len(L)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if L[j] < L[min_index]:
                min_index = j
        # min_index is the minimum in L[i+1:length]
        if min_index != i:
            L[i],L[min_index] = L[min_index],L[i]
    return(L)

selection_sort([3,1,4,2,6,3])  

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def search(self,key):
        L = self
        while L and L.data != key:
            L = L.next
        return L
    
    def search2(self,key):
        L = self
        while L:
            if L == key:
                return L
            else:
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
head1 = None
tail = head1
for x in L:
    if head1 is None:
        head1 = ListNode(x)
        tail = head1
    else:
        tail.next = ListNode(x)
        tail = tail.next
head1.print_LL()
a = ListNode(100)
head1.insert_after(a)
head1.print_LL()




l = [2,4,6,8,10]
head = None
tail = head
for i in l:
    if head == None:
        head = ListNode(i)
        tail = head 
    else:
        tail.next = ListNode(i)
        tail = tail.next

current = head
while current:
    print(current.data)
    current = current.next



# BinaryTreeNode
class BTN:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def search(self,key): #return node with value key
        # if equal - > return the node
        # elif key < node -> find from the left
        # else -> find from teh right
        if self.data == key:
            return self
        elif self.data < key:
            #make sure self.left is not None
            if self.left:
                return self.left.search(key)
        else:
            # find form right tree
            if self.right:
                return self.right.search(key)

    def insert(self,new_node):
        # find the Node s.t. ket <= Node.data & Node.left ==None
        # or key > Node & Node.right is None
        if new_node.data <= self.data:
            if self.left is None:
                self.left = new_node 
                new_node.parent = self
            else:
                return self.left.insert(new_node)
        else: # new_node.data < self.data
            if self.right is None: 
                self.right = new_node 
                new_node.parent = self
            else:
                return self.right.insert(new_node)
                
    def find_minimum(self):
        # if the node.left is None : return node
        min_node = self
        while min_node.left:
            min_node = min_node.left
        return min_node

    def find_maximum(self):
        max_node = self
        while max_node.right:
            max_node = max_node.right
        return max_node

    def tree_traversal(self):
        # inordre 
        if self.left:
            self.left.tree_traversal()
        print(self.data,end=" ")
        if self.right:
            self.right.tree_traversal()

        # Reveiw the ways of teraversal
    
    def create(self,sequence,index):
        if index >= len(sequence) or sequence[index] == None:
            return None
        else:
            tempNode = BTN(sequence[index])
            tempNode.left = self.create(sequence,2*index+1)
            tempNode.right = self.create(sequence,2*index+2)
            tempNode.parent = self
            return tempNode




    