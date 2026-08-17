class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        beginTime = newInterval[0]
        res = []
        currIndex = 0

        for interval in intervals:
            if interval[1] < beginTime:
                res.append(interval)
                currIndex += 1
            else:
                break
        
        currMerge = newInterval
        for i in range(currIndex, len(intervals)):

            if currMerge[1] < intervals[i][0]:
                break

            if currMerge[0] <= intervals[i][1]:
                currMerge = [min(intervals[i][0], currMerge[0]), max(currMerge[1], intervals[i][1])]
            currIndex += 1
        
        res.append(currMerge)

        for i in range(currIndex, len(intervals)):
            res.append(intervals[i])
        

        return res
        
        