# 994. Rotting Oranges.py
"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])

        q = collections.deque()

        good_num = 0

        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    good_num += 1
        count = 0

        direction = [[0,1],[0,-1],[1,0],[-1,0]]

        while good_num > 0 and q:
            length = len(q)
            for _ in range(length):

                q_pop = q.popleft()
                for d in direction:
                    di,dj = q_pop[0]+d[0],q_pop[1]+d[1]
                    if di in range(Rows) and dj in range(Cols) and grid[di][dj] == 1:
                        
                        q.append((di,dj))
                        grid[di][dj] = 2
                        good_num -= 1

            count += 1
        
        return count if good_num == 0 else -1










