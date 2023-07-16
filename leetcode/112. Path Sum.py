# 112. Path Sum.py
"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 """

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# create a list named L and contain all the possible path sum
# then check wheather targetSum in L or not
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        L = []
        def helper(root,sum): #contain all path sum in this tree
            if not root: # the tree is empty
                return
            if not root.left and not root.right: # it is the leaf node
                L.append(sum+root.val)
            
            if root.left:
                helper(root.left,sum+root.val)
            if root.right:
                helper(root.right,sum+root.val)
        helper(root,0)

        return targetSum in L


# By recursive  and Keep adjusting the targetSum dynamically 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        else: 
            return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)