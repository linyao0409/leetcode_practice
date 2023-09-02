"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        
        def dfs(index, tempSum):
            if tempSum > target:
                return
            if tempSum == target:
                res.append(path.copy())
                return
            
            if index >= len(candidates):
                return
            
            # Include current candidate
            path.append(candidates[index])
            dfs(index+1, tempSum + candidates[index])
            path.pop()
            
            # Skip duplicates
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, tempSum)

        dfs(0, 0)
        return res