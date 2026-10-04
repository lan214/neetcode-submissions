from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minCost(i):
            if i < 2:
                return 0
            return min(
                cost[i-1] + minCost(i-1),
                cost[i-2] + minCost(i-2)
            )
        return minCost(len(cost))