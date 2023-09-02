"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        count = 0
        if n == 0:
            return len(tasks)
        
        # greddy
        # create a dictionary about frequency
        d = {}
        for x in tasks:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        d["idle"] = 0
        print(d)

        # find the most frequency and use it 
        # and suspend using it for k times

tasks = ["A","A","A","B","B","B"]
n = 2
a = Solution()
a.leastInterval(tasks,n)