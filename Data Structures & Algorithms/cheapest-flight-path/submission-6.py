class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # prices = [math.inf] * n
        # prices[src] = 0

        # for _ in range(k+1):
        #     tmp = prices.copy()
        #     for s, d, c in flights:
        #         if prices[s] == math.inf:
        #             continue
        #         if prices[s] + c < prices[d]:
        #             tmp[d] = prices[s] + c
        #     prices = tmp
        
        # return prices[dst] if prices[dst] != math.inf else -1

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]