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
        count = 0
        for i in nums:
            if evenOrNot(i):
                count += 1
        return count
