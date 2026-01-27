"""
Problem: LeetCode 739 - Daily Temperatures
Pattern: Monotonic Stack (Decreasing)
Key Idea:
- For each day, find how many days until a warmer temperature
- Stack stores indices of decreasing temperatures

Approach:
- Traverse temperatures array
- Maintain a decreasing stack of indices
- When current temperature > temperature at stack top:
    - Pop index and calculate days difference

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)

        return res
