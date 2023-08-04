# 450. Delete Node in a BST
"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        3 cases
            1. delete leaf node
            2. delete node with 1 child
            3. delete node with 2 children
        """
        if not root:
            return
        
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            # case 1 and 2 - root is a leaf node or has a single child
            if not root.right or not root.left: 
                return root.right or root.left
            
            #case 3 both children
            successor = root.right

            # find successor
            while successor.left:
                successor = successor.left

            root.val = successor.val
            root.right = self.deleteNode(root.right, root.val)
                    
        return root

        