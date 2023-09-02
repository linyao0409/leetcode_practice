# 572. Subtree of Another Tree.py
"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_same_tree(root1,root2):
            if (root1 is None) and (root2 is None):
                return True
            if (root1 is None) or (root2 is None):
                return False
            
            if (root1.val != root2.val):
                return False
            
            return check_same_tree(root1.left,root2.left) and check_same_tree(root1.right,root2.right)

        # do traversal

        # if there is a node with the same value of subtree's root
        # -> check_same_tree(this node,subtree's root)
        def dfs(root1,root2):
            if not root1:
                return False
            if root1.val == root2.val and check_same_tree(root1,root2):
                return True
            else:
                return dfs(root1.left,root2) or dfs(root1.right,root2)
        
        return dfs(root,subRoot)



        
