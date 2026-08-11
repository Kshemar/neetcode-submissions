class WordDictionary:

    def __init__(self):
        self.children = {}
        self.eow = False

    def addWord(self, word: str) -> None:
        for c in word:
            if c not in self.children:
                self.children[c] = WordDictionary()
            self = self.children[c]
        self.eow = True

    def search(self, word: str) -> bool:
        return self.dfs(self, word, 0)

    def dfs(self, node, word, i) -> bool:
        if i == len(word):
            return node.eow
        if word[i]=='.':
            for child in node.children.values():
                if self.dfs(child,word,i+1):
                    return True
            return False

        if word[i] not in node.children:
            return False

        return self.dfs(node.children[word[i]], word, i+1)