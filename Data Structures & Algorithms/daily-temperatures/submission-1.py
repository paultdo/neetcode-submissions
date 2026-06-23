class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                if temperatures[i] <= temperatures[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and temperatures[i] > temperatures[stack[-1]]:
                        first_index = stack[-1]
                        stack.pop()
                        results[first_index] = i - first_index
                    stack.append(i)
        
        for i in stack:
            results[i] = 0
        
        return results
