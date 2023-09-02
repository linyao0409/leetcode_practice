# 110. Balanced Binary Tree.py

"""
Given a binary tree, determine if it is 
height-balanced
.
"""
# Definition for a binary tree node.  # class TreeNode: #     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Height-Balanced
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0

            left_h = height(root.left)
            right_h = height(root.right)

            if abs(left_h - right_h) > 1:
                self.boolval = False
                
            return max(left_h,right_h) + 1

        self.boolval = True
        height(root)
        return  self.boolval

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 不用全部跑完一次 跑到abs(left-right) > 1滿足 return -1時就停止 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            

        return check(root) != -1
        
        
        
