"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
# Definition for a binary tree node.  # class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inTheTree(root,target):
            if not root:
                return False
            if root == target:
                return True
            
            return inTheTree(root.left,target) or inTheTree(root.right,target)
        
        if root == p or root == q:
            return root
        
        indexLeft = inTheTree(root.left,p) or inTheTree(root.left,q)
        indexRight = inTheTree(root.right,p) or inTheTree(root.right,q)

        if indexLeft and indexRight:
            return root
        
        if indexLeft:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)

                
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_v = p.val
        q_v = q.val

        if p_v > q_v:
            p_v,q_v = q_v,p_v
        
        node = root
        while node:
            cv = node.val
            if cv == p_v or cv == q_v:
                return node
            indexLeft = cv >= p_v
            indexRight = cv <= q_v
            
            if indexLeft and indexRight:
                return node
            if indexLeft:
                node = node.left
            else:
                node = node.right

                

            








            






