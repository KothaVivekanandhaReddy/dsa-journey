"""
Problem: LeetCode 452 - Minimum Number of Arrows to Burst Balloons
Pattern: Greedy (Intervals)
Key Idea:
- One arrow can burst all balloons that overlap at a point
- To minimize arrows, always shoot at the earliest possible end

Approach:
- Sort intervals by end coordinate
- Shoot the first arrow at the end of the first interval
- For each next interval:
    - If it overlaps with current arrow position → continue
    - Else → need a new arrow, update arrow position

Time Complexity: O(n log n)
Space Complexity: O(1) (ignoring sort space)
"""

class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort balloons by end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            # If current balloon starts after arrow position, need new arrow
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows
