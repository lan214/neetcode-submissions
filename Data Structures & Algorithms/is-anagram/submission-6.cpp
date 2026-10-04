#include <ranges>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;

        std::unordered_map<char, int> count;
        for (std::size_t i {0}; i < s.size(); ++i) {
            ++count[s[i]];
            --count[t[i]];
        }
        
        return std::ranges::all_of(count | std::views::values, [](int n) {return n == 0;});
    }
};
