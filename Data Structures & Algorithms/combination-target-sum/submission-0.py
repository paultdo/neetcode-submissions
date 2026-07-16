class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sums = []
        def dfs(curr, index):

            if curr == target:
                res.append(sums.copy())
                return

            if index >= len(nums):
                return

            if curr > target:
                return
            
            curr += nums[index]
            sums.append(nums[index])
            dfs(curr, index)

            sums.pop()
            dfs(curr - nums[index], index + 1)
        
        dfs(0, 0)

        return res
