class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = nums[0]
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            newSum = dp[i - 1] + nums[i]
            dp[i] = max(newSum, nums[i])
            currSum = max(currSum, dp[i])
        
        return currSum