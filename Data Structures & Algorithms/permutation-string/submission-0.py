from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq = Counter(s1)
        l = 0
        distinct_size = len(freq)
        for r in range(len(s2)):
            if s2[r] in freq:
                freq[s2[r]] -= 1
                if freq[s2[r]] == 0:
                    distinct_size -= 1
                    if distinct_size == 0:
                        return True
                while freq[s2[r]] < 0:
                    freq[s2[l]] += 1
                    if freq[s2[l]] == 1:
                        distinct_size += 1
                    l += 1
            else:
                while l < r:
                    if s2[l] in freq:
                        freq[s2[l]] += 1
                        if freq[s2[l]] == 1:
                            distinct_size += 1
                    l += 1
                l += 1
        return False
