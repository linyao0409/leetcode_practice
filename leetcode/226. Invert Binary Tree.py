# 226. Invert Binary Tree.py

"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mirror(root):
 
    if (root == None):
        return
 
    q = []
    q.append(root)
    while (len(q)):

        curr = q[0]
        q.pop(0)
 
        curr.left, curr.right = curr.right, curr.left

        if (curr.left):
            q.append(curr.left)
        if (curr.right):
            q.append(curr.right)
            
# better one
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 
            root.left,root.right = root.right,root.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root
        

            
