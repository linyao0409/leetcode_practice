# Course Schedule II.py
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for x in prerequisites:
            prereq[x[0]].append(x[1]) 
        
        
        visited = set()
        inAns = set()
        res = []

        def dfs(cur):
            if cur in inAns:
                return True
            if cur in visited:
                return False


            visited.add(cur)
            
            for pre in prereq[cur]:
                if not dfs(pre):
                    return False
            visited.remove(cur)

            res.append(cur)
            inAns.add(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
            
                       