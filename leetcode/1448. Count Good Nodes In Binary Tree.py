"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0 
        tempMax = root.val

        def dfs(root,tempMax):
            if not root:
                return
            if root.val >= tempMax:
                self.count += 1
                tempMax = root.val
            dfs(root.left,tempMax)
            dfs(root.right,tempMax)
        
        dfs(root,tempMax)
        return self.count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        count = 0
        
        def dfs(node,tempMax):
            nonlocal count
            if not node:
                return
            if node.val >= tempMax:
                count += 1
                tempMax = node.val
            dfs(node.left,tempMax)
            dfs(node.right,tempMax)
        

        dfs(root,root.val)
        return count
            
        
                







        