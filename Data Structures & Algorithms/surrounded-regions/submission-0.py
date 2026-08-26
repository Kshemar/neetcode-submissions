class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def bfs(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or
            (r,c) in visit or board[r][c]=="X"):
                return
            visit.add((r,c))
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)

        for r in range(ROWS):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][COLS-1] == "O":
                bfs(r, COLS-1)
        for c in range(COLS):
            if board[0][c] == "O":
                bfs(0, c)
            if board[ROWS-1][c] == "O":
                bfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visit:
                    board[r][c] = "X"        