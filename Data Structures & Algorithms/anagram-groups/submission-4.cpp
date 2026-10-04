class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> map;
        for (auto &str: strs) {
            auto key = str;
            std::sort(key.begin(), key.end());
            map[key].push_back(str);
        }
        std::vector<vector<string>> result;
        for (auto &[_, value]: map) {
            result.push_back(std::move(value));
        }
        return result;
    }
};
