class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []

        res = list()
        for l in range(len(nums) - k + 1):
            r = l + k
            res.append(max(nums[l:r]))
        
        return res