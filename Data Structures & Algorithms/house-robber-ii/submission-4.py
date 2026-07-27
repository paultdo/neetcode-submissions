class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums) + 1)
        cache2 = [-1] * (len(nums) + 1)

        if len(nums) == 1:
            return nums[0]

        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]

            maximum = max(nums[i] + dfs(i + 2), dfs(i + 1))
            cache[i] = maximum

            return cache[i]
        def dfs2(i):
            if i >= len(nums) - 1:
                return 0
            if cache2[i] != -1:
                return cache2[i]

            maximum = max(nums[i] + dfs2(i + 2), dfs2(i + 1))
            cache2[i] = maximum

            return cache2[i]
        
        return max(dfs(1), dfs2(0))