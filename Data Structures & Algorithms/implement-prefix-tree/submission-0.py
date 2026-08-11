class PrefixTree:

    def __init__(self):
        self.children = {}
        self.eow = False

    def insert(self, word: str) -> None:
        for c in word:
            if c not in self.children:
                self.children[c] = PrefixTree()
            self = self.children[c]
        self.eow = True

    def search(self, word: str) -> bool:
        for c in word:
            if c not in self.children:
                return False
            self = self.children[c]
        return self.eow 
        
    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            if c not in self.children:
                return False
            self = self.children[c]
        return True
        
        