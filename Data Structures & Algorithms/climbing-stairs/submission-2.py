class Solution:
    def climbStairs(self, n: int) -> int:
        self.count = 0
        self.cache = [0] * (n+1)
        def recursion(curr):
            if curr > n:
                return 0

            if self.cache[curr] != 0:
                return self.cache[curr]

            if curr == n:
                return 1

            numWays = recursion(curr + 1) + recursion(curr + 2)
            self.cache[curr] = numWays
            return numWays
        
        return recursion(0)