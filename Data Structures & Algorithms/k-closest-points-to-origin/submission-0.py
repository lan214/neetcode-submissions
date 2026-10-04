class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, point in enumerate(points):
            heapq.heappush_max(max_heap, (self.dist(point), i))
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)
        return [points[i] for _, i in max_heap]
        
    def dist(self, point: List[int]) -> float:
        return point[0]**2 + point[1]**2