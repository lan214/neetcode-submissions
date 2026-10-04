class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        l = 0
        max_length = 0
        for r, c in enumerate(s):
            while seen[c] > 0:
                seen[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, (r - l) + 1)
            seen[c] += 1
        
        return max_length
            
