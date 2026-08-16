class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

    def inc(self,word):
        for ch in word:
            if ch not in self.children:
                self.children[ch]=TrieNode()
            self = self.children[ch]
        self.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.inc(w)
        row,col = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):
            if (r<0 or c<0 or r==row or c==col or 
            board[r][c] not in node.children or (r,c) in visit):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.eow:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)
