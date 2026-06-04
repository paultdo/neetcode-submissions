class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0] * len(nums)
        result = []
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append((prefix[i - 1] * nums[i]))
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = (postfix[i + 1] * nums[i])
        
        for i in range(0, len(nums)):
            if i == 0:
                result.append(1 * postfix[i+1])
            elif i == (len(nums) - 1):
                result.append(1 * prefix[i-1])
            else:
                result.append(prefix[i-1] * postfix[i + 1])

        
        return result
        
