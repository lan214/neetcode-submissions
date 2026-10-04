class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        result = []

        while top < bottom and left < right:
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])
            right -= 1
            if not (top < bottom and left < right):
                break
            for col in reversed(range(left, right)):
                result.append(matrix[bottom - 1][col])
            bottom -= 1
            for row in reversed(range(top, bottom)):
                result.append(matrix[row][left])
            left += 1
        return result