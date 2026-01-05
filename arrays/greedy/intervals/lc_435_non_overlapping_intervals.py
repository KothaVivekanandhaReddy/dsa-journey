"""
Problem: LeetCode 435 - Non-overlapping Intervals
Pattern: Greedy (Intervals)
Key Idea:
- To remove minimum intervals, keep intervals that end earliest
- Earlier end leaves more room for future intervals

Approach:
- Sort intervals by end time
- Keep track of the end of the last selected interval
- If current interval overlaps, remove it
- Else, update the end pointer

Time Complexity: O(n log n)
Space Complexity: O(1) (ignoring sort space)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap → remove current interval
                removals += 1
            else:
                prev_end = end

        return removals
