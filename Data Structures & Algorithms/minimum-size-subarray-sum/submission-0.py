class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minCount = 0
        total = 0

        rFlag = True
        while r < len(nums):
            if rFlag:
                total += nums[r]
                rFlag = False
            if total >= target:
                minCount = min(minCount, r - l + 1) if minCount != 0 else r - l + 1
                r += 1
                rFlag = True
                while total >= target:
                    total -= nums[l]
                    l += 1
                    minCount = min(minCount, r - l + 1) if minCount != 0 else r - l + 1
            elif total < target:
                r += 1
                rFlag = True
        
        return minCount


