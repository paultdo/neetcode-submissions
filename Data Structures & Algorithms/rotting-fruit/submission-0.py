class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            currSize = len(q)
            rotFlag = False
            for i in range(currSize):
                curr = grid[q[0][0]][q[0][1]]
                r = q[0][0]
                c = q[0][1]
                q.popleft()
                if curr == 0:
                    continue
                
                if curr == 1:
                    grid[r][c] = 2
                    rotFlag = True
                
                up = down = left = right = None
                if r + 1 < ROWS:
                    up = (r + 1, c)
                if r - 1 >= 0:
                    down = (r - 1, c)
                if c + 1 < COLS:
                    right = (r, c + 1)
                if c - 1 >= 0:
                    left = (r, c - 1)

                if up and up not in seen:
                    q.append(up)
                    seen.add(up)
                if down and down not in seen:
                    q.append(down)
                    seen.add(down)
                if right and right not in seen:
                    q.append(right)
                    seen.add(right)
                if left and left not in seen:
                    q.append(left)
                    seen.add(left)
            if rotFlag:
                time += 1
            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time 
        
