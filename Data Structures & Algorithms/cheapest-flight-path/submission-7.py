class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for _ in range(k+1):
            tmp = prices.copy()
            for s, d, c in flights:
                if prices[s] == math.inf:
                    continue
                if prices[s] + c < tmp[d]:
                    tmp[d] = prices[s] + c
            prices = tmp
        
        return prices[dst] if prices[dst] != math.inf else -1