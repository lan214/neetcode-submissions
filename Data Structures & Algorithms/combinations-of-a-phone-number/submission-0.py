class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtrack(i, word):
            if i == len(digits):
                res.append("".join(word))
                return
            for char in mapping[digits[i]]:
                word.append(char)
                backtrack(i+1, word)
                word.pop()
        
        backtrack(0, [])
        return res