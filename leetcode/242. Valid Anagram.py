# 242. Valid Anagram.py

""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length1 = len(s)
        length2 = len(t)

        if length1 != length2:
            return False

        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in t:
            if i not in d:
                return False
            else: 
                d[i] -= 1
                if d[i] == 0:
                    del d[i]

        return True



        
        
        