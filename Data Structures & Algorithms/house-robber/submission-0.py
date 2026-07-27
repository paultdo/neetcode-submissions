class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums))

        def dfs(i):
            if i >= len(nums) or i < 0:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            

            maximum = max(dfs(i + 1), nums[i] + dfs(i + 2))
            if cache[i] == -1:
                cache[i] =  maximum
            
            return cache[i]
        
        return max(dfs(0), dfs(2))
        