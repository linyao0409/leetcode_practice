#684. Redundant Connection.py
"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 """

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        length = len(edges)
        connections = {i:[] for i in range(1,length+1)}

        for x in edges:
            connections[x[0]].append(x[1])
        
        # start from 1

        visited = set()
        #certain = set()
        res = []

        def dfs(cur):
            #if cur in certain:
                #return True
            if cur in visited:
                res.append(cur)
                return False
            visited.add(cur)
            
            for c in [x for x in connections[cur] if x > cur]:
                if not dfs(c):
                    res.append(cur)
                    return False # ?
            visited.remove(cur)
        
        dfs(0)
        res.reverse()
        return res

            
            


