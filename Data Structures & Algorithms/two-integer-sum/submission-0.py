class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in hashMap:
                return [hashMap.get(difference), i]

            hashMap.update({nums[i]: i})
        
        
