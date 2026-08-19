class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []

        res_counter = 0
        for i in range(len(intervals)):
            interval = intervals[i]
            if i == 0:
                res.append(interval)
                res_counter += 1
                continue

            prev_interval = res[res_counter - 1]

            if interval[0] <= prev_interval[1]:
                if interval[1] > prev_interval[1]:
                    res[res_counter - 1][1] = interval[1]
            else:
                res.append(interval)
                res_counter += 1
        
        return res
            
            
