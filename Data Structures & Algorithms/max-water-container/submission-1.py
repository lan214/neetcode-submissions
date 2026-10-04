class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            h_l = heights[l]
            h_r = heights[r]
            max_area = max(max_area, min(h_l, h_r) * (r - l))
            if h_r > h_l:
                l += 1
            else:
                r -= 1
        return max_area