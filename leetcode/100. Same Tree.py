# 100. Same Tree.py

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root1,root2):
            if root1 is None and root2 is None: # both none
                return True
            if root1 is None or root2 is None: # one side None -> return False
                return False

            if root1.val != root2.val: # check value
                return False
            
            if  dfs(root1.left,root2.left) == False or dfs(root1.right,root2.right) == False:
                return False 
            
            #return True
        
        return dfs(p,q) != False


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        
        return dfs(p, q)
