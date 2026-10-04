"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x : x.start)
        min_heap = [intervals[0].end]
        res = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            res = max(res, len(min_heap))
        return res
            
