"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (not preorder) or (not inorder):
            return None
        
        node_val = preorder[0]
        root = TreeNode(node_val)


        mid = inorder.index(node_val)

        root.left = self.buildTree(preorder=preorder[1:mid+1],inorder = inorder[:mid])
        root.right = self.buildTree(preorder=preorder[mid+1:],inorder = inorder[mid+1:])
        return root