class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 
        rows, cols = len(grid), len(grid[0])
        visit = set()
        if not grid:
            return 0
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                dirs = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in dirs:
                    r,c = row + dr, col + dc
                    if(r in range(rows) and c in range(cols) and 
                    (r,c) not in visit and grid[r][c] == 1):
                        q.append((r,c))
                        visit.add((r,c))
                        area += 1
            return area
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 1:
                    res = max(res, bfs(r,c))
        return res

            