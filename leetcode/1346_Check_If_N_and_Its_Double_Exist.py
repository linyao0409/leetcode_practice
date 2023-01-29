#1346_Check_If_N_and_Its_Double_Exist.py
#Given an array arr of integers, check if there exist two indices i and j such that :

"""i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]"""
#my solution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for x in arr:
            if x * 2 in s or x/2 in s:
                return True
            s.add(x)
        return False
#using set(list)
class Solution:
    def checkIfExist(self, A: List[int]) -> bool:
        if A.count(0) > 1: return True
        S = set(A) - {0}
        for a in A:
            if 2*a in S: return True
        return False

        
        
