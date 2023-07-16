#102. Binary Tree Level Order Traversal.py

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 """

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list1=[]
        q=deque()
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                poping=q.popleft()
                if poping:
                    level.append(poping.val)
                    q.append(poping.left)
                    q.append(poping.right)
            if level:
                list1.append(level)
        return list1
    #please upvote me it would encourage me alot


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        list1 = []
        q = []
        q.append(root)

        while(q):
            level = []
            for i in range(len(q)):
                popping = q.pop(0)
                if popping:
                    level.append(popping.val)
                    q.append(popping.left)
                    q.append(popping.right)
            if level:
                list1.append(level)
        return list1
            



# 429. N-ary Tree Level Order Traversal
"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = []
        list1 = []
        q.append(root)

        while(q):
            level = []
            for i in range(len(q)):
                popping = q.pop(0)
                if popping:
                    level.append(popping.val)
                    for child in popping.children:
                        q.append(child)
                
            if level:
                list1.append(level)
        
        return list1
