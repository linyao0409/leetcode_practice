"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        LevelOrder = []
        q = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                temp = q.pop(0)
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            LevelOrder.append(level)
        
        ans = []
        for x in LevelOrder:
            ans.append(x[-1])
        return ans 
