class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False
        
        def insert(self, word: str):
            current = self
            for c in word:
                if c not in current.children:
                    current.children[c] = WordDictionary.TrieNode()
                current = current.children[c]
            current.is_word = True
        
        def is_present(self, word: str, i: int):
            if i == len(word):
                return self.is_word
            c = word[i]
            if c not in self.children and c !='.':
                return False
            if c != '.':
                return self.children[c].is_present(word, i + 1)
            for node in self.children.values():
                print("here")
                if node.is_present(word, i + 1):
                    return True
            return False

    def __init__(self):
        self.trie = self.TrieNode()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.is_present(word, 0)
        
