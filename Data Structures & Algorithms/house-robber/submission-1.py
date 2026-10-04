from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(
                dfs(i-1),
                nums[i] + dfs(i-2),
            )
        return dfs(len(nums) - 1)

        n = len(nums)
        dp = [0] * 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[0], dp[1] = dp[1], max(dp[1], nums[i] + dp[0])
        return dp[1]

