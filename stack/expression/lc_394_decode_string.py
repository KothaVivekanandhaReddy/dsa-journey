"""
Problem: LeetCode 394 - Decode String
Pattern: Stack (Nested State)
Key Idea:
- Use stack to store previous string and repetition count

Approach:
- When '[' appears, push (current_string, count)
- When ']' appears, pop and expand
- Digits build the repetition count

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += ch

        return curr_str
