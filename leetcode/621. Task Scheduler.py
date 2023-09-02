"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""

import collections
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = collections.Counter(tasks)
        MaxHeap = [-x for x in d.values()]
        heapq.heapify(MaxHeap)

        q = collections.deque()
        time = 0

        while MaxHeap or q:
            time += 1
            if not MaxHeap:
                time = q[0][1]
            else:
                temp = heapq.heappop(MaxHeap)
                if temp+1 != 0:
                    q.append([temp+1,time+n])
            if q and time == q[0][1]:
                a = q.popleft()
                heapq.heappush(MaxHeap,a[0])
        return time


