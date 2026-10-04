class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0] * n 
        curr_max = 0
        for i, h in enumerate(height):
            curr_max = max(h, curr_max)
            l_max[i] = curr_max
        r_max = [0] * n
        curr_max = 0
        for i in range(n-1, -1, -1):
            curr_max = max(height[i], curr_max)
            r_max[i] = curr_max

        trapped = 0
        for i in range(1, n - 1):
            water = min(l_max[i], r_max[i]) - height[i]
            trapped += water if water > 0 else 0
        return trapped

