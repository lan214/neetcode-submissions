class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_up, row_down = 0, len(matrix) - 1
        col_left, col_right = 0, len(matrix[0]) - 1
        result = []
        while row_up <= row_down or col_left <= col_right:
            if row_up <= row_down:
                for col in range(col_left, col_right + 1):
                    result.append(matrix[row_up][col])
                row_up += 1
            if col_left <= col_right:
                for row in range(row_up, row_down + 1):
                    result.append(matrix[row][col_right])
                col_right -= 1
            if row_up <= row_down:
                for col in range(col_right, col_left - 1, -1):
                    result.append(matrix[row_down][col])
                row_down -= 1
            if col_left <= col_right:
                for row in range(row_down, row_up - 1, -1):
                    result.append(matrix[row][col_left])
                col_left += 1
        return result