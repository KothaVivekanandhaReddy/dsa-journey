"""
Problem: LeetCode 3439 - Maximum Free Time I
Pattern: Greedy (Intervals / Merge Intervals)
Key Idea:
- Merge overlapping intervals
- Maximum free time is the largest gap between consecutive merged intervals

Approach:
- Zip start and end times into intervals
- Sort by start time
- Merge intervals while tracking previous end
- 1.build intervals
- 2.sort
- 3.build gaps
- 4.sliding window
- 5.return max gap

Time Complexity: O(n log n)
Space Complexity: O(n) (for sorting/interval list)
"""
from ast import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        intervals = list(zip(startTime,endTime))
        intervals.sort(key=lambda x : x[0])
        gaps = []
        gaps.append(intervals[0][0]-0)
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            gaps.append(start-prev_end)
            prev_end = max(prev_end,end)

        gaps.append(eventTime-prev_end)
        wind_size = k +1 
        curr_sum = sum(gaps[:wind_size])
        max_free = curr_sum

        for i in range(wind_size,len(gaps)):
            curr_sum += gaps[i]
            curr_sum -= gaps[i-wind_size]
            max_free = max(max_free,curr_sum)
        return max_free