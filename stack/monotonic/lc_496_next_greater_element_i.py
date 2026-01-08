"""
Problem: LeetCode 496 - Next Greater Element I
Pattern: Monotonic Stack (Decreasing)
Key Idea:
- Maintain a decreasing stack
- When a larger element is found, it is the next greater for stack elements

Approach:
- Traverse nums2
- Use a stack to track decreasing elements
- When current > stack top, pop and map next greater
- Use hashmap to answer queries for nums1

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Remaining elements have no next greater
        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]
