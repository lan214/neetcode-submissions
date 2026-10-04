class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValid(row):
                return False
        
        for i_col in range(9):
            if not self.isValid(board[i_row][i_col] for i_row in range(9)):
                return False
        
        for i_col in range(0, 9, 3):
            for i_row in range(0, 9, 3):
                if not self.isValid(board[i_row + j][i_col + h] for j in range(3) for h in range(3)):
                    return False
        
        return True
        
    def isValid(self, iterable: Iterable[str]) -> bool:
        seen = [False] * 9
        for s in iterable:
            if s.isnumeric():
                if seen[int(s) - 1]:
                    return False
                seen[int(s) - 1] = True
        return True
