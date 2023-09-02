# 130. Surrounded Regions.py
"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        h = len(board)
        w = len(board[0])

        def dfs(i,j):
            if i<0 or i>=j or j<0 or j>=w or board[i][j] != "O":
                return 
            board[i][j] = "#"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        #first row 
        i = 0
        for j in range(w):
            dfs(i,j)
        i = h-1
        for j in range(w):
            dfs(i,j)

        j = 0
        for i in range(1,h-1):
            dfs(i,j)
        
        j = w-1
        for i in range(1,h-1):
            dfs(i,j)
        
        for i in range(h):
            for j in range(w):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
