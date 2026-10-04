class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::unordered_map<int, int> count;
        for (size_t i {0}; i < s.size(); ++i) {
            count[s[i]]++;
            count[t[i]]--;
        }
        for (auto const& [_, value] : count) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    }
};
