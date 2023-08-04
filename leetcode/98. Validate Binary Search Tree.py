# 98. Validate Binary Search Tree.py
"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        comp_L = True
        comp_R = True
        
        if root.left:
            comp_L = root.val > root.left.val
        if root.right:
            comp_R = root.val < root.right.val
        if not(comp_L and comp_R):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, -inf, inf)

class Solution:
    order = []
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        order.append(root.val)
        self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return sorted(order) == order

class Solution:
    def isValidBST(self,root):
        def helper(node,low,high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(root.left,low,node.val) and helper(root.right,node.val,high)
        return helper(root,-inf,inf)
            