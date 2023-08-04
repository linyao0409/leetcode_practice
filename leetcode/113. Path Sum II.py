# 113. Path Sum II.py
"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        L = []
        l = []
        def dfs(root,targetSum):
            if not root:
                return
            if not root.left and not root.right:
                l.append(root.val)
                if targetSum == root.val:
                    L.append(l)
            else:
                l.append(root.val)
                if root.left:
                    dfs(root.left,targetSum-root.val)
                    l.pop()
                if root.right:
                    dfs(root.right,targetSum-root.val)
                    l.pop()
        dfs(root,targetSum)
        return L

