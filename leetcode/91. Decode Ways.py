# 91. Decode Ways.py
"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""


class Solution:
    def numDecodings(self, s: str) -> int:

        length = len(s)
        if length == "0":
            return 0
        elif length == 1 and s[0]=="0":
            return  0
        elif length == 1 and s[0] != "0":
            return 1
        elif length == 2 and s[0] == "0":
            return 0
        elif length ==2 and  s[1] == "0":
            if 0 <= int(s) <= 26:
                return 1
            else:
                return 0
        elif length == 2 and int(s) > 26:
            return 1
        elif length > 2 and int(s[-2:]) == 0:
            return 0
        
        # length >= 3
        df = [0] * length

        index = length-1

        if s[index] == "0":
            if int(s[-2:]) > 26:
                return 0
            df[-1] = 0
            df[-2] = 1
        elif s[index-1] == "0":
            df[-1] = 1
            df[-2] = 0
        elif int(s[-2:]) <= 26:
            df[-1] = 1
            df[-2] = 2
        else:
            df[-1] = 1
            df[-2] = 1

        index = length - 3
        while index >= 0:
            if s[index] == "0":
                df[index] = 0
            elif int(s[index:index+2]) > 26:
                df[index] = df[index+1]
            else:
                df[index] = df[index+1] + df[index+2]
            
            index -= 1
        return df[0]

