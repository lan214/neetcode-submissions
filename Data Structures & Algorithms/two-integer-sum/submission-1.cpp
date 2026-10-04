class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen{};
        for (int i {0}; i < nums.size(); ++i) {
            int num = nums[i];
            int complement = target - num;
            if (seen.find(complement) != seen.end()) {
                return std::vector<int> {seen[complement], i};
            }
            seen.insert({num, i});
        }
        return std::vector<int>{-1, -1};
    }
};
