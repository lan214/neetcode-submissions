class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        trapped = 0
        for r in range(len(height)):
            if height[r] >= height[l]:
                min_height = height[l]
                while l < r:
                    trapped += min_height - height[l]
                    l += 1
        r = len(height) - 1
        for l in range(len(height) - 1, -1, -1):
            if height[l] > height[r]:
                min_height = height[r]
                while l < r:
                    trapped += min_height - height[r]
                    r -= 1
        return trapped

