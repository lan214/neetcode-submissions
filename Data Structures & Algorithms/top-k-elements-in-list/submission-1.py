from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequency = []
        elements = [(v, k) for k, v in count.items()]
        for item in elements:
            heapq.heappush(frequency, item)
            if len(frequency) > k:
                heapq.heappop(frequency)
        return [item[1] for item in frequency]