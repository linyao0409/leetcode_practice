# 941_Valid_Mountain_Array.py

"""Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]"""

#my code
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        n = len(arr)
        if n < 3:
            return False
        i = 0
        j = n-1
        index  = True
        stopIndex = 0
        while(i != j and stopIndex < 3):
            if(index):
                index = False
                stopIndex += 1
                if arr[i] < arr[i+1]:
                    i += 1
                    stopIndex = 0
                    
            else:
                index = True
                stopIndex += 1
                if arr[j] < arr[j-1]:
                    j -= 1
                    stopIndex = 0
        if i == j and i != 0 and j != n-1:
            return True
        else:
            return False



# better way
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <3:
            return False
        left_max = arr[0]
        left_index = 0
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                left_index = i-1
                break
        right_max = arr[-1]
        right_index = len(arr) - 1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] <= arr[i+1]:
                right_index = i+1
                break
        return left_index == right_index
            
