class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [-1] * len(s)
        wordSet = set(wordDict)

        def dfs(i):
            if i > len(s) - 1 or i < 0:
                return True
            if cache[i] != -1:
                return cache[i]
            
            substr = s[:i + 1]
            wordFound = False
            for j in range(len(substr)):
                if s[j:i+1] in wordSet and dfs(j - 1):
                    wordFound = True
                
            if not wordFound:
                cache[i] = False
                return False
            else:
                cache[i] = True
                return True
        
        return dfs(len(s) - 1)
            

