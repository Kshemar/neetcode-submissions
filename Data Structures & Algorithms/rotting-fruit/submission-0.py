class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        minutes, fresh = 0, 0

        def convert(r,c):
            nonlocal fresh
            if(r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]!=1):
                return 
            grid[r][c] = 2
            fresh-=1
            q.append((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                convert(r+1,c)
                convert(r,c+1)
                convert(r-1,c)
                convert(r,c-1)
            minutes+=1
        if fresh == 0:
            return minutes
        return -1