# 79. Word Search.py
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def neighbor(i, j, s):
            res = []
            if i > 0 and board[i - 1][j] == s:
                res.append([i - 1, j])
            if i < h - 1 and board[i + 1][j] == s:
                res.append([i + 1, j])
            if j > 0 and board[i][j - 1] == s:
                res.append([i, j - 1])
            if j < w - 1 and board[i][j + 1] == s:
                res.append([i, j + 1])
            return res

        def check(xhead, yhead, word_1):
            visited[xhead][yhead] = False
            if len(word_1) == 0:
                return True
            neighbors = neighbor(xhead, yhead, word_1[0])
            if len(neighbors) == 0:
                visited[xhead][yhead] = True  # Reset visited status before return
                return False
            for x in neighbors:
                if visited[x[0]][x[1]]:
                    if check(x[0], x[1], word_1[1:]):
                        return True
            visited[xhead][yhead] = True  # Reset visited status after all neighbors are checked
            return False

        if not board:
            return False
        h = len(board)
        w = len(board[0])

        head = word[0]
        head_list = []

        for i in range(h):
            for j in range(w):
                if board[i][j] == head:
                    head_list.append([i, j])

        for headPoint in head_list:
            visited = [[True] * w for i in range(h)]
            if check(headPoint[0], headPoint[1], word[1:]):
                return True
        return False



            
        


