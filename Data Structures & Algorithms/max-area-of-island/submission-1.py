class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maximum = 0

        def destroy(row, col):
            if row >= ROWS or col >= COLS or row < 0 or col < 0:
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return 1 + destroy(row + 1, col) + destroy(row - 1, col) + destroy(row, col + 1) + destroy(row, col - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr = destroy(r,c)
                    maximum = max(maximum, curr)
        
        return maximum