# 20. Valid Parentheses.py
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 """

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for x in s:
            if x == ')':
                if len(l)!=0 and l[-1] == '(': #len(l) != 0 prevent sceriero ")" it might emerge index error 
                    l.pop()
                else:
                    return False

            elif x == '}':
                if len(l)!=0 and l[-1] == '{':
                    l.pop()
                else:
                    return False

            elif x == ']':
                if len(l)!=0 and l[-1] == '[':
                    l.pop()
                else:
                    return False
            else:
                l.append(x)

        if len(l) == 0:
            return True

        
