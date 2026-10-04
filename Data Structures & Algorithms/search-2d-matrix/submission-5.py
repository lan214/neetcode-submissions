class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        u, d = 0, len(matrix) - 1
        while u <= d:
            mid = u + (d - u) // 2
            if matrix[mid][0] < target:
                u = mid + 1
            elif matrix[mid][0] > target:
                d = mid - 1
            else:
                return True
        
        if d < 0:
            return False
        
        l, r = 0, len(matrix[d]) - 1
        while l <= r:
            mid = (l + r) // 2
            print((l,r,mid))
            if matrix[d][mid] < target:
                l = mid + 1
            elif matrix[d][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False