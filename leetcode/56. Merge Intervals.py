# 56. Merge Intervals.py
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
# time exceed
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlapOrNot(x1,x2,a,b):
            l1 = x2 - x1
            l2 = b-a
            maxL = max(abs(x1-a),abs(x2-b),abs(a-x2),abs(b-x1),abs(b-a),abs(x2-x1))
            if maxL <= l1 + l2:
                return True
            else:
                return False

        if len(intervals) <= 0:
            return [] 
        else:
            result = [intervals[0]]
            for x in intervals[1:]:
                temp = []
                for y in result:
                    if overlapOrNot(x[0],x[1],y[0],y[1]):
                        x[0] = min(x[0],y[0])
                        x[1] = max(x[1],y[1])
                        #result.remove(y)
                        temp.append(y)
                for d in temp:
                    result.remove(d)
                result.append(x)
        return result



# accept but too slow
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a = [i for i,j in intervals]
        b = [j for i,j in intervals]

        minMum = min(a)
        maxMum = max(b)
        length = maxMum - minMum 
        array = [0] * length
        for a,b in intervals:
            l = a - minMum
            r = b - minMum
            if l == r:
                continue
            for i in range(l,r):
                array[i] = 1
        result = []
        x1,x2 = 0,0
        index = False
        #chech [a,a] condition
        temp = []
        for a,b in intervals:
            if a == b:
                if a in temp:
                    continue
                temp.append(a)
                if a-minMum == 0:
                    if array[a-minMum] == 0:
                        result.append([a,a])
                elif a-minMum == length:
                    if array[a-minMum-1] == 0:
                        result.append([a,a])
                else:
                    if array[a-minMum] == 0 and array[a-minMum-1] == 0:
                        result.append([a,a])


        for i in range(length):
            if array[i] == 0:
                if index:
                    result.append([x1+minMum,x2+minMum+1])
                x1,x2 = i,i
                index = False
            else:
                if  not index:
                    x1,x2 = i,i
                else:
                    x2 = i
                index = True
        if array[-1] == 1:
            result.append([x1+minMum,x2+minMum+1])
                
        return result

# better solution
            
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key = lambda interval:interval[0])

        result = []
        x1,x2 = sorted_intervals[0][0],sorted_intervals[0][1]
        for a,b in sorted_intervals[1:]:
            if a <= x2 and b > x2:
                x2 = b
            elif a<= x2 and b <= x2:
                continue
            else:
                result.append([x1,x2])
                x1,x2 = a,b 

        result.append([x1,x2])
        return result














