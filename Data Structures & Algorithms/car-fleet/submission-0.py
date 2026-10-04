class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(p, (target - p)/s) for p,s in zip(position, speed)]
        times.sort(reverse=True)
        stack = []
        for _, time in times:
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)