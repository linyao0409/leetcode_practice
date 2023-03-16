# 424. Longest Repeating Character Replacement.py
"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findmax(d:dict)->int:
            maximum = 0
            for key in d:
                if d[key] >= maximum:
                    maximum = d[key]
            return maximum
        # create a hashtable
        
        chars = {}
        for x in s:
            if x not in chars:
                chars[x]  = 0
        
        l = 0
        r = 0
        length = len(s)
        len_win = 1
        ans = 0
        while r < length:
            chars[s[r]] += 1
            if len_win - findmax(chars) <= k:
                if len_win > ans:
                    ans = len_win
                len_win += 1
            else:
                chars[s[l]] -= 1
                l += 1
            r += 1
        return ans
            