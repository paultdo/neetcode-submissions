class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i != len(temperatures) - 1:
                j = i + 1
                while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                    j += 1
                
                if j < len(temperatures) and temperatures[j] > temperatures[i]:
                    result[i] += j - i
        return result


