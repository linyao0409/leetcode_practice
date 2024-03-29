# 94. Binary Tree Inorder Traversal.py
"""Given the root of a binary tree, return the inorder traversal of its nodes' values.

 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Approach
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,A):
            if root:
                helper(root.left,A)
                A.append(root.val)
                helper(root.right,A)
        A = []
        helper(root,A)
        return A

#Iterating method using Stack
class Solution:
    def inorderTraversal(self,root):
        L = []
        stack = []
        
        curr = root
        while(curr or len(stack) != 0):
            while(curr):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            L.append(curr.val)
            curr = curr.right
        return L

#144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L = []

        def helper(root):
            if not root:
                return
            L.append(root.val)

            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
        
        helper(root)
        return root
            


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L = []
        def helper(root):
            if  not root:
                return 
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
            L.append(root.val)
        helper(root)
        return L
            