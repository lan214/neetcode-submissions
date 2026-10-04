class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        auto size = nums.size();
        vector<int> res(size*2, 0);
        for (size_t i{0}; i < size; ++i) {
            res[i] = nums[i];
            res[i + size] = nums[i];
        }
        return res;
    }
};