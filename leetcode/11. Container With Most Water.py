# 11. Container With Most Water.py
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

#:跑太慢了

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def value(x1,x2):
            width = x2 - x1
            h = min(height[x2] , height[x1])
            return width * h
        length = len(height)
        tempMax  = value(0,length-1)
        index_left = 0
        index_right = length-1 
        
        for i in range(0,length):
            # skip i s.t. height[i] <= height[index_left]
            if height[i] < height[index_left]:
                continue
            index_right = length-1
            for j in range(length-1,i,-1):
                
                if height[j] < height[index_right]:
                    continue
                temp = value(i,j)
                if temp >= tempMax:
                    tempMax = temp
                    index_left = i
                    index_right = j
        return tempMax

# 學這個就好
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ansMax = 0
        length = len(height)
        l,r = 0,length-1
        while l<r:
            wide = r-l
            h = min(height[r],height[l])
            temp = wide * h
            if ansMax < temp:
                ansMax = temp
            if height[l] <= height[r]:#比較低的才去移動他的index
                l += 1
            else:
                r -= 1
        return ansMax