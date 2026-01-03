"""
Problem: LeetCode 53 - Maximum Subarray
Pattern: Kadane’s Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]

        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            max_sum = max(max_sum, curr_sum)

        return max_sum
