class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        currMax = dp[0]
        currMin = dp[0]

        for i in range(1, len(nums)):
            candidates = [nums[i], nums[i] * currMax, nums[i] * currMin]
            currMax = max(candidates)
            currMin = min(candidates)
            dp[i] = max(currMax, dp[i - 1])
        
        return dp[len(nums) - 1]

