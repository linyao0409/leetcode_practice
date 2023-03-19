# 200. Number of Islands.py
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] != '1':
                return 
            # i ,j in legal range and grid[i][j]  == '1'
            grid[i][j] = '#'
            dfs(grid,i-1,j) #up
            dfs(grid,i+1,j) #down
            dfs(grid,i,j-1) #left
            dfs(grid,i,j+1) #right
        
        height = len(grid)
        width = len(grid[0])
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid,i,j)
        return count
        