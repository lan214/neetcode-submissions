class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = self.dfs(grid, row, col)
                    max_area = max(max_area, area)
        
        return max_area

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 2
        return 1 + self.dfs(grid, row + 1, col) + self.dfs(grid, row - 1, col) + self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)
        