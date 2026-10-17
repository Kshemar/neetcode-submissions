class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visit = set()

        def dfs(r,c):
            if(r<0 or r>=rows or c<0 or c>=cols or (r,c)in visit or grid[r][c]==0):
                return 0
            visit.add((r,c))
            curr = 1
            curr+=dfs(r+1,c)
            curr+=dfs(r,c+1)
            curr+=dfs(r-1,c)
            curr+=dfs(r,c-1)
            return curr

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    area = max(area, dfs(r,c))
        return area