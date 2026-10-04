class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        n = len(s)

        def is_palindrome(word):
            n = len(word)
            i = 0
            while i < n - i - 1:
                if word[i] != word[n - i - 1]:
                    return False
                i += 1
            return True

        def backtrack(i, current_split: list[str]):
            if i == len(s):
                if is_palindrome(current_split[-1]):
                    res.append(current_split[::])
                return
            
            word = []
            for k in range(i, n):
                word.append(s[k])
                if is_palindrome(word):
                    current_split.append("".join(word))
                    backtrack(k + 1, current_split)
                    current_split.pop()
        
        backtrack(0, [])
        return res