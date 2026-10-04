class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                res = max(res, price - min_price)
        return res