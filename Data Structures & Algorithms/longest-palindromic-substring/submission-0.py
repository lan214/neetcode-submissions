class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            result = (left, left - 1)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result = (left, right)
                left -= 1
                right += 1
            return result

        if not s:
            return ""

        result = (0,0)
        for i in range(len(s)):
            left, right = expand(s, i, i)
            if right - left > result[1] - result[0]:
                result = (left, right)
            left, right = expand(s, i, i+1)
            if right - left > result[1] - result[0]:
                result = (left, right)
            print(result)
        
        return s[result[0]:result[1]+1]
