"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid)

        def dfs(i,j):
            global count
            if i<0 or i>=h or j<0 or j>=w or grid[i][j] != 1:
                return 
            
            grid[i][j] = "#"
            count += 1
            dfs(i-1,j) # up
            dfs(i+1,j) # down
            dfs(i,j-1)
            dfs(i,j+1)
        
        global count
        max = 0
        for i in range(h):
            for j in range(w):
                count = 0
                dfs(i,j)
                if count > max:
                    max = count
        return max

# 不用全域變數的寫法 把count當return 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] != 1:
                return 0

            grid[i][j] = "#"
            count = 1
            count += dfs(i - 1, j)  # 上
            count += dfs(i + 1, j)  # 下
            count += dfs(i, j - 1)  # 左
            count += dfs(i, j + 1)  # 右

            return count

        max_area = 0
        for i in range(h):
            for j in range(w):
                current_count = dfs(i, j)
                if current_count > max_area:
                    max_area = current_count
        return max_area
