class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high
        while low <= high:
            rate = low + (high - low) // 2
            time = self.compute_time(piles, rate)
            if time <= h:
                high = rate - 1
            else:
                low = rate + 1
        return low
    
    def compute_time(self, piles, rate):
        time = 0
        for pile in piles:
            time += math.ceil(pile / rate)
        return time