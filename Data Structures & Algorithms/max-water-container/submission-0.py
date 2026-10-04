class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area