class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        op, cl = 0, 0 

        def backtrack(op, cl, cur):
            if op == cl == n: 
                res.append(cur)
                return
            if op < n:
                backtrack(op + 1, cl, cur + '(')
            if cl < op:
                backtrack(op, cl + 1, cur + ')')
        backtrack(0,0,"")
        return res
