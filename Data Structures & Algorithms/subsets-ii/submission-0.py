class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        nums = sorted(nums)

        def dfs(index):
            if index > len(nums) - 1:
                res.append(sub.copy())
                return;
            
            sub.append(nums[index])
            dfs(index + 1)

            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            
            sub.pop()
            dfs(index + 1)
        
        dfs(0)

        return res
