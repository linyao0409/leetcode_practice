# 5. Longest Palindromic Substring.py
"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length_len = 0

        for i in range(len(s)):
            l,r = i,i
            # odd case
            while l>= 0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > length_len:
                    res = s[l:r+1]
                    length_len = r-l+1
                l-=1
                r+=1

            # even case
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 >length_len:
                    res = s[l:r+1]
                    length = r-l+1
                l-=1
                r+=1

        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            ans = max(ans, expand(s, i, i), expand(s, i, i + 1), key=len)
        
        return ans
            

def expand(s, i, j):
    len_s = len(s)

    while i >= 0 and j < len_s and s[i] == s[j]:
        i -= 1
        j += 1 
    
    return s[i+1:j]