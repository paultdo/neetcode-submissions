class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            newSum = prev + nums[i]
            prev = max(newSum, nums[i])
            currSum = max(currSum, prev)
        
        return currSum