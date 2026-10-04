from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [val for val in freq.values()]
        heapq.heapify_max(max_heap)
        res = 0
        stack = []
        while max_heap:
            task_count = heapq.heappop_max(max_heap)
            task_count -= 1
            res += 1
            task_count and stack.append(task_count)
            if not stack and not max_heap:
                break
            for _ in range(n):
                res += 1
                if max_heap:
                    next_task_count = heapq.heappop_max(max_heap)
                    next_task_count -= 1
                    next_task_count and stack.append(next_task_count)
                if not stack:
                    break

            while stack:
                heapq.heappush_max(max_heap, stack.pop())
        return res


