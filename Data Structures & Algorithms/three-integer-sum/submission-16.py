class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            first_num = nums[i]

            while left < right:
                sum1 = first_num + nums[left] + nums[right]
                if sum1 > 0:
                    right -= 1
                elif sum1 < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        
        return result