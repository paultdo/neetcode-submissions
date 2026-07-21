class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []
        def dfs(i):
            if i >= len(s):
                res.append(parts.copy())
                return

            for j in range(i, len(s)):
                substr = s[i:j + 1]
                if substr == substr[::-1]:
                    parts.append(substr)
                    dfs(j + 1)
                    parts.pop()
        
        dfs(0)

        return res

