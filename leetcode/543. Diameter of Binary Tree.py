# 543. Diameter of Binary Tree.py

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 算處左右子樹最高長度相加 
# 持續更新直徑
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            
            left_h = height(root.left)
            right_h = height(root.right)

            self.d = max(self.d,left_h+right_h)
            return max(left_h,right_h) + 1


        self.d = 0
        height(root)
        return self.d

