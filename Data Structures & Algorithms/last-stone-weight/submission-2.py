import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones[:]
        heapq.heapify_max(max_heap)
        while len(max_heap) > 1:
            diff = heapq.heappop_max(max_heap) - heapq.heappop_max(max_heap)
            if diff > 0:
                heapq.heappush_max(max_heap, diff)
        return max_heap[0] if len(max_heap) > 0 else 0