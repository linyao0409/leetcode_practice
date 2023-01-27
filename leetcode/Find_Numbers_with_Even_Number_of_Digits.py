# Find_Numbers_with_Even_Number_of_Digits.py
class Solution:
    # write a function to determine wheather it is a even digit or not
    def findNumbers(self, nums: List[int]) -> int:
        def evenOrNot(x):
            x = len(str(x))
            if x % 2 == 0:
                return True  # if yes, return true
            else:
                return False  # if false, return false
            #return not x&1  use this to determine  even or not
            #  x&1 if x is enen return 0
            #      if x is odd return 1
            #not x&1 return true if x is even
        count = 0
        for i in nums:
            if evenOrNot(i):
                count += 1
        return count
        
