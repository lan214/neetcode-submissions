class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for c1,c2 in zip(s, t):
            count_s[c1] = count_s.get(c1, 0) + 1
            count_t[c2] = count_t.get(c2, 0) + 1
        return count_s == count_t
        