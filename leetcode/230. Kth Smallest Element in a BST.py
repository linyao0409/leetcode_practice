# 230. Kth Smallest Element in a BST.py
"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #length = 0
        l = []
        
        def dfs(node):
            #nonlocal length
            if len(l) >= k:
                return 
            if not node:
                return

            dfs(node.left)

            if len(l) < k:
                l.append(node.val)

            dfs(node.right)
        
        dfs(root)
        return l[-1]
            
            


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if count >= k:
                return 
            if not node:
                return

            dfs(node.left)

            if count < k:
                count += 1
                if count == k:
                    self.kthMax = node.val

            dfs(node.right)
        
        dfs(root)
        return self.kthMax 
            
            
