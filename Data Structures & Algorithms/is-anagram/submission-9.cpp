#include <ranges>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        std::unordered_map<char, int> count;
        for (size_t i{0}; i < s.size(); ++i) {
            count[s[i]] += 1;
            count[t[i]] -= 1;
        }
        for (const auto &c : std::views::values(count)) {
            if (c != 0) return false;
        }
        return true;
    }
};
