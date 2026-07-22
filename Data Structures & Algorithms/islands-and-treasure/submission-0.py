class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = (2 ** 31) - 1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def bfs():
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        q.append((r, c, 0))
            seen = set()
            while q:
                curr = grid[q[0][0]][q[0][1]]
                r = q[0][0]
                c = q[0][1]
                dist = q[0][2]

                q.popleft()
                if curr == -1:
                    continue

                if curr == inf:
                    grid[r][c] = dist

                
                up = None
                down = None
                left = None
                right = None

                if r + 1 < ROWS:
                    up = (r + 1, c, dist + 1)
                    up_set = (r + 1, c)
                
                if r - 1 >= 0:
                    down = (r - 1, c, dist + 1)
                    down_set = (r-1, c)
                
                if c + 1 < COLS:
                    right = (r, c + 1, dist + 1)
                    right_set = (r, c + 1)
                
                if c - 1 >= 0:
                    left = (r, c - 1, dist + 1)
                    left_set = (r, c- 1)

                if up and up_set not in seen:
                    q.append(up)
                    seen.add(up_set)
                if down and down_set not in seen:
                    q.append(down)
                    seen.add(down_set)
                if left and left_set not in seen:
                    q.append(left)
                    seen.add(left_set)
                if right and right_set not in seen:
                    q.append(right)
                    seen.add(right_set)

        bfs()
        

                

            
        
        

            
            

