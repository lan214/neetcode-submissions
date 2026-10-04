QUEEN = -1
VALID = 0

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[0] * n for _ in range(n)]
        res = []

        def getGridOutput():
            res = []
            for row in range(n):
                part = []
                for col in range(n):
                    if grid[row][col] == QUEEN:
                        part.append("Q")
                    else:
                        part.append(".")
                res.append("".join(part))
            return res

        def backtrack(remaining_to_place, row, column):
            for r in range(row, n):
                for c in range(n):
                    # placer la reine et invalider les row, col, diags
                    if grid[r][c] == VALID:
                        grid[r][c] = QUEEN
                        for i in range(n):
                            if grid[r][i] != QUEEN:
                                grid[r][i] += 1
                            if grid[i][c] != QUEEN:
                                grid[i][c] += 1
                        i  = 1
                        while r-i >= 0 and c-i >= 0:
                            grid[r-i][c-i] += 1
                            i += 1
                        i  = 1
                        while r+i < n and c+i < n:
                            grid[r+i][c+i] += 1
                            i += 1
                        while r-i >= 0 and c+i < n:
                            grid[r-i][c+i] += 1
                            i += 1
                        i  = 1
                        while r+i < n and c-i >= 0:
                            grid[r+i][c-i] += 1
                            i += 1
                        if remaining_to_place == 1:
                            res.append(getGridOutput())
                        else:
                            backtrack(remaining_to_place-1, r+1, c)

                        # enlever la reine et revalider les row, col, diags
                        for i in range(n):
                            if grid[r][i] != QUEEN:
                                grid[r][i] -= 1
                            if grid[i][c] != QUEEN:
                                grid[i][c] -= 1
                        i  = 0
                        while r-i >= 0 and c-i >= 0:
                            grid[r-i][c-i] -= 1
                            i += 1
                        i  = 0
                        while r+i < n and c+i < n:
                            grid[r+i][c+i] -= 1
                            i += 1
                        while r-i >= 0 and c+i < n:
                            grid[r-i][c+i] -= 1
                            i += 1
                        i  = 1
                        while r+i < n and c-i >= 0:
                            grid[r+i][c-i] -= 1
                            i += 1
                        grid[r][c] = VALID

        backtrack(n, 0, 0)
        return res
