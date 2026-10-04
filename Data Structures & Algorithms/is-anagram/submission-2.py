class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = defaultdict(int)
        for c in s:
            count_s[c] += 1

        for c in t:
            if c not in count_s:
                return False
            count_s[c] -= 1

        for count in count_s.values():
            if count != 0:
                return False
                
        return True
        