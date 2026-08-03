class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_d= set()
        neg_d= set()
        res = []
        part = [["."] *n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in part]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in pos_d or (r-c) in neg_d:
                    continue
                col.add(c)
                pos_d.add(r+c)
                neg_d.add(r-c)
                part[r][c] = "Q"
                backtrack(r+1)
                #undo
                col.remove(c)
                pos_d.remove(r+c)
                neg_d.remove(r-c)
                part[r][c] = "."
        
        backtrack(0)
        return res
                
        

        