class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_brackets = 0
        close_brackets = 0

        par_string = ""
        res = []

        def dfs(open, close, par_string):
            if open == n and close == n:
                res.append(par_string[:])
                return
            
            if open < n:
                dfs(open + 1, close, par_string + "(")

            if close < open:
                dfs(open, close + 1, par_string + ")")
        dfs(open_brackets, close_brackets, par_string)

        return res


            

            
            
