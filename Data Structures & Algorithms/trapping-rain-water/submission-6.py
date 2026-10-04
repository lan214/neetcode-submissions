class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        result = 0
        
        while l < r:
            if leftMax < rightMax:
                result += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                result += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])

        return result

