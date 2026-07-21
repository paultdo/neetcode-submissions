class Solution:
    maximum = 0
    curr = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def destroy(row, col):
            if row >= ROWS or col >= COLS or row < 0 or col < 0:
                return
            
            if grid[row][col] == 0:
                return
            
            grid[row][col] = 0
            self.curr += 1
            self.maximum = max(self.maximum, self.curr)

            destroy(row + 1, col)
            destroy(row - 1, col)
            destroy(row, col + 1)
            destroy(row, col - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.curr = 0
                    destroy(r,c)
        
        return self.maximum