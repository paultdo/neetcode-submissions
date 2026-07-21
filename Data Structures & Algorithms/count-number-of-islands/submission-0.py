class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        def destroy(row, col):
            if row >= ROWS or col >= COLS or row < 0 or col < 0:
                return

            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            destroy(row + 1, col)
            destroy(row - 1, col)
            destroy(row, col + 1)
            destroy(row, col - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    destroy(r, c)
                    count += 1
        
        return count