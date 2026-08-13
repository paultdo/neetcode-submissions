class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        cache = {}
        def dfs(i, targ):
            if i == len(nums):
                return False

            if (i, targ) in cache:
                return cache[(i, targ)]
            
            if targ == (sum(nums) / 2):
                return True
            
            res = dfs(i + 1, targ) or dfs(i + 1, targ + nums[i])

            cache[(i, targ)] = res
            
            return res
        
        return dfs(0, 0)
