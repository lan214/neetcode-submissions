class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::ranges::sort(nums);
        for (std::ptrdiff_t i{0}; i < std::ssize(nums) - 1; ++i) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }
};