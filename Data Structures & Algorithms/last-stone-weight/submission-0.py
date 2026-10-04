import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones[:]
        heapq.heapify_max(max_heap)
        while len(max_heap) > 1:
            heapq.heappush_max(max_heap, heapq.heappop_max(max_heap) - heapq.heappop_max(max_heap))
        return max_heap[0]