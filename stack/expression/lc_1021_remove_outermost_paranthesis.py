"""
Problem: LeetCode 1021 - Remove Outermost paranthesis
Pattern: stack
Key Idea:
- Track : depth = how many waiting
- decision : for '(' -> add when depth>0
-            for ')' -> add when depth>1

Approach:
- depth = 0 
- for each char :
-     if '(':
-        if depth>0: add  to res
-        depth += 1
-     else:
-        depth -= 1
-        if depth>0: add  to res
- return res
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = []

        for ch in s:
            if ch == '(':
                if stack:
                    res.append(ch)
                stack.append(ch)
            else:
                stack.pop()
                if stack:
                    res.append(ch)

        return "".join(res)
    
