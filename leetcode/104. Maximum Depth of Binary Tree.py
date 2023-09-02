# 104. Maximum Depth of Binary Tree.py
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_max(root):
            # if root.left & root.right both null -> return 1
            # if root == None reutnr 0
            if (not root):
                return 0
            
            return max(find_max(root.left) , find_max(root.right)) + 1
        
        return find_max(root)

