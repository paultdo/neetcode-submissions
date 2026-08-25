"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key= lambda i: i.start)
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        ends = sorted(ends)

        count = 0
        maxCount = count

        s = 0
        e = 0

        if not intervals:
            return 0

        while s < len(starts):
            if starts[s] >= ends[e]:
                    count -= 1
                    e += 1
            while starts[s] < ends[e]:
                s += 1
                count += 1
                maxCount = max(maxCount, count)
                if s == len(starts):
                    break
        
        return maxCount



