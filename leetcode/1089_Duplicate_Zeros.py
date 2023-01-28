#Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

#Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

#        "Do not return anything, modify arr in-place instead."
#1089_Duplicate_Zeros.py
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        count = 0
        indexBool = False
        for i in arr:
            if i==0:
                count += 1
        newLength = length + count

        for i in range(length):
            if indexBool:
                indexBool = False
                arr.pop()
                continue
            if arr[i] == 0:
                arr.insert(i+1,0)
                indexBool = True
            else:
                indexBool = False
            arr.pop()
            
            
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        length = len(arr)
        while i<length-1:
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i+=1
            i+=1
