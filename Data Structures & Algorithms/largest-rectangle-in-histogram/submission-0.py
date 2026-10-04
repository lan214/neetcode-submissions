class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            j = i
            while stack and stack[-1][0] > height:
                h, j = stack.pop()
                max_area = max(max_area, h * (i - j))
            stack.append((height, j))
        while stack:
            h, j = stack.pop()
            max_area = max(max_area, h * (n - j))
        
        return max_area