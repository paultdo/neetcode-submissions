class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, prev) -> int:
            if i == len(nums) or i < 0:
                return 0
            
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            branch1 = dfs(i + 1, prev)
            branch2 = 1 + dfs(i + 1, i) if prev == -1 or nums[i] > nums[prev] else 0
            
            cache[(i, prev)] = max(branch1, branch2)

            return cache[(i, prev)]
        
        return dfs(0, -1)

            
            

            
            