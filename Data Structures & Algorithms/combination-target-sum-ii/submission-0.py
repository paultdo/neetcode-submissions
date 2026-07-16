class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        sums = []
        candidates = sorted(candidates)
        def dfs(index, curr):

            if curr == target:
                res.append(sums.copy())
                return
            
            if index >= len(candidates) or curr > target:
                return

            
            curr += candidates[index]
            sums.append(candidates[index])
            dfs(index + 1, curr)

            distinct = candidates[index]
            while index < len(candidates) and candidates[index] == distinct:
                index += 1

            curr -= distinct
            sums.pop()
            dfs(index, curr)
        
        dfs(0, 0)
        return res