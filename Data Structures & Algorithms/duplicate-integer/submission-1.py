class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            if num not in numsSet:
                numsSet.add(num)
            else:
                return True
        return False