class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_length = 0
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            
            max_length = max(max_length, (r - l) + 1)
            seen.add(c)
        
        return max_length
            
