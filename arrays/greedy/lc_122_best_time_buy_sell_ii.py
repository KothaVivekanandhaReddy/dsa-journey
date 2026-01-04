"""
Problem: LeetCode 121 - Best Time to Buy and Sell Stock
Pattern: Greedy (Kadane-style intuition)
Key Idea:
- Track the minimum price so far
- At each day, compute best profit if selling today

Approach:
- Maintain min_price seen so far
- Update max_profit using current_price - min_price

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
