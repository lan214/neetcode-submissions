class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::unordered_map<char, int> charCount;
        for (char c: s) {
            if (!charCount.contains(c)) {
                charCount[c] = 0;
            }
            charCount[c]++;
        }
        for (char c: t) {
            if (!charCount.contains(c)) {
                return false;
            }
            charCount[c]--;
        }
        for (const auto& [_, v]: charCount) {
            if (v != 0) {
                return false;
            }
        }
        return true;
    }
};
