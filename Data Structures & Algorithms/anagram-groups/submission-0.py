class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            anagrams = groups.get(key, [])
            anagrams.append(word)
            groups[key] = anagrams
        return groups.values()