class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for a, b in zip(word1, word2):
            res.append(a)
            res.append(b)
        size1 = len(word1)
        size2 = len(word2)
        if size1 < size2:
            res.append(word2[size1:])
        else:
            res.append(word1[size2:])
        return "".join(res)