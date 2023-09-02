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
            if level:
                LevelOrder.append(level)
        
        ans = [x[-1] for x in LevelOrder]

        return ans 
################################################################################################
"""
你的演算法使用了 level order traversal (即層次遍歷) 來解決問題，並取出每層的最後一個元素，這是正確的方法來找出從右邊看到的節點。但有幾個地方可以改進：

使用deque而非list: q.pop(0) 在Python的 list 上運行的時間複雜度為 O(n)，這對於大型輸入可能會造成效能瓶頸。相反地，使用 collections.deque 可以使 pop 操作具有 O(1) 的時間複雜度。

不需要存儲完整的層次結構: 你其實只需要每層的最右邊的值，所以可以直接添加它而不是每次都添加整個層次。
"""
################################################################################################

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            size = len(q)
            # 我們只關心這一層的最後一個節點
            for i in range(size):
                node = q.popleft()
                # 直接在迴圈中加入最右邊的節點，不需要保存整個層次
                if i == size - 1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans


