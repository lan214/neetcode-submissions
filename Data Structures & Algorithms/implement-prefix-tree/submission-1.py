class PrefixTree:

    def __init__(self):
        self.children = defaultdict()
        self.is_word = False
        

    def insert(self, word: str) -> None:
        if not word:
            return
        currentTree = self
        for c in word:
            if c not in currentTree.children:
                currentTree.children[c] = PrefixTree()
            currentTree = currentTree.children[c]
        currentTree.is_word = True


    def search(self, word: str) -> bool:
        currentTree = self
        for c in word:
            currentTree = currentTree.children.get(c)
            if currentTree is None:
                return False
        return currentTree.is_word
        

    def startsWith(self, prefix: str) -> bool:
        currentTree = self
        for c in prefix:
            currentTree = currentTree.children.get(c)
            if currentTree is None:
                return False
        return True
        
        