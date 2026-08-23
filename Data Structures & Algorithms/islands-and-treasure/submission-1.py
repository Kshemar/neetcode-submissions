class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def addgrid(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
            (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0
        #going through queue
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist # =0
                addgrid(r+1, c)
                addgrid(r, c+1)
                addgrid(r-1, c)
                addgrid(r, c-1)
            dist +=1
