class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = dict()
        l = 0
        max_length = 0
        for r, c in enumerate(s):
            if c in last_seen:
                l = max(last_seen[s[r]] + 1, l)
            max_length = max(max_length, r - l + 1)
            last_seen[c] = r
        
        return max_length
            
