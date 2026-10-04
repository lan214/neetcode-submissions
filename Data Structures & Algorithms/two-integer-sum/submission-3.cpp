#include <ranges>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::ptrdiff_t> seen;
        for (const auto& [i, num]: std::views::enumerate(nums)) {
            int toFind = target - num;
            if (seen.contains(toFind)) {
                return {static_cast<int>(seen[toFind]), static_cast<int>(i)};
            }
            seen[num] = i;
        }
        return {-1, -1};
    }
};
