class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        substr = ""

        def dfs(i, sub):
            if i >= len(digits):
                res.append(sub[:])
                return
            
            for c in nums[digits[i]]:
                sub += c
                dfs(i + 1, sub)
                sub = sub[0:len(substr) - 1]

        dfs(0, substr)

        return res if digits else []