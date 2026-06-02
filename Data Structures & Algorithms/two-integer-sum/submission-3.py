class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [hash_map[complement], i]
            