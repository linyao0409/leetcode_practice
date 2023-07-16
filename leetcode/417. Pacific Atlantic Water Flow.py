# 417. Pacific Atlantic Water Flow.py
"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def Pacific(heights,i,j,matrix,val=0):
            # out of range or the value if less than the value tyour eant toyo compare
            # return directly 
            if i<0 or i>=h or j<0 or j>=w or heights[i][j]<val or matrix[i][j] == 1:
                return
            # 位置合理 而且可以到海邊
            matrix[i][j] = 1
            Pacific(heights,i-1,j,matrix,heights[i][j])
            Pacific(heights,i+1,j,matrix,heights[i][j])
            Pacific(heights,i,j-1,matrix,heights[i][j])
            Pacific(heights,i,j+1,matrix,heights[i][j])

        def Atl(heights,i,j,matrix2,val=0):
            if i<0 or i>=h or j<0 or j>=w or heights[i][j]<val or matrix2[i][j] == 1:
                return
            # 位置合理 而且可以到海邊
            matrix2[i][j] = 1
            Atl(heights,i-1,j,matrix2,heights[i][j])
            Atl(heights,i+1,j,matrix2,heights[i][j])
            Atl(heights,i,j-1,matrix2,heights[i][j])
            Atl(heights,i,j+1,matrix2,heights[i][j])
        h = len(heights)
        w = len(heights[0])
        matrix = [[0]*w for i in range(h)]
        matrix2 = [[0]*w for i in range(h)]
        # first row
        i = 0
        for j in range(w):
            Pacific(heights,i,j,matrix)
        # first col
        j = 0
        for i in range(h):
            Pacific(heights,i,j,matrix)

        # lastest row
        i = h-1
        for j in range(w):
            Atl(heights,i,j,matrix2)
        # lastest col
        j = w-1
        for i in range(h):
            Atl(heights,i,j,matrix2)
        
        result = []
        for i in range(h):
            for j in range(w):
                if matrix[i][j] and matrix2[i][j]:
                    result.append([i,j])
        return result
        
        
            


