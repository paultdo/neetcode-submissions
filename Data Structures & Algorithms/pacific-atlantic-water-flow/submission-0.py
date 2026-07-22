class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # see what nodes can reach pacific ocean and what nodes can reach atlantic
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, ocean, prev):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (prev != -1 and heights[r][c] < prev) or (r,c) in ocean:
                return
            
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        
        #loop through pacific
        for r in range(ROWS):
            for c in range(COLS):
                if c > 0 and r > 0:
                    break
                elif c == 0 or r == 0:
                    dfs(r, c, pacific, -1)
        
        #loop through atlantic
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if c < COLS - 1 and r < ROWS - 1:
                    break
                elif c == COLS - 1 or r == ROWS - 1:
                    dfs(r, c, atlantic, -1)
        
        common = pacific & atlantic

        res = []
        for pair in common:
            res.append(list(pair))

        return res




