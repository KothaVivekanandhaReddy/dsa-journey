"""
Problem: LeetCode 20 - Valid Parentheses
Pattern: Stack (Matching)
Key Idea:
- Opening brackets must be closed in correct order

Approach:
- Push opening brackets onto stack
- On closing bracket, check top of stack
- Stack must be empty at the end

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mapping:
                if not stack :
                    return False
                top = stack.pop()
                if top != mapping[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
