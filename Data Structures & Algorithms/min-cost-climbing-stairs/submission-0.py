class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0] * (len(cost) + 1)

        def dfs(i):
            if i >= len(cost):
                return 0

            if cache[i] != 0:
                return cache[i]

            minimum = min(dfs(i + 1), dfs(i + 2))
            if cache[i] == 0:
                cache[i] = cost[i] + minimum
            
            return cache[i]
        return min(dfs(0), dfs(1))