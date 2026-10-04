class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * 2
        for i in range(2, n + 1):
            dp[0], dp[1] = dp[1], min(
                cost[i-1] + dp[1],
                cost[i-2] + dp[0]
            )
        return dp[1]
