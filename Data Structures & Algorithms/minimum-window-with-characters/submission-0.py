class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq_t = Counter(t)
        l = 0
        freq_s = defaultdict(int)
        distinct_match = len(freq_t)
        res = (-1,-1)
        for r in range(len(s)):
            freq_s[s[r]] += 1
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                distinct_match -= 1
                    
            while distinct_match == 0:
                if res[0] == -1 or res[1] - res[0] > r - l:
                    res = (l, r)
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] == freq_t[s[l]] - 1:
                    distinct_match += 1
                l += 1
        return s[res[0]:res[1]+1]