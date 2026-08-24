class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[0] < prevEnd:
                count += 1
                prevEnd = min(prevEnd, interval[1])
            else:
                prevEnd = interval[1]
        
        return count
            



