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
        
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, -inf, inf)

# slow 
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.indicator = True

        def dfs(node):

            if not node:
                return True
            if node.left:
                if node.left.val > node.val:
                    self.indicator = False
            if node.right:
                if node.right.val < node.val:
                    self.indicator = False
                #return False
            if self.indicator:
                return dfs(node.left) or dfs(node.right)
            else:
                return False
        
        return dfs(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.indicator = True
        def helper(node,low,high):
            if not node:
                return True
            if self.indicator:
                if low < node.val < high:
                    return helper(node.left,low,node.val) and helper(node.right,node.val,high)
                else:
                    self.indicator = False
            else:
                return False
        
        return helper(root,float("-inf"),float("inf"))
                

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            
            # If the current node does not satisfy the BST condition
            if not (low < node.val < high):
                return False
            
            # Check left and right sub-trees
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, float("-inf"), float("inf"))
