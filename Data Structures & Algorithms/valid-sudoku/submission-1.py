class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                if not value.isnumeric():
                    continue

                if (value in rows[r]
                    or value in cols[c]
                    or value in boxes[(r // 3) * 3 + c // 3]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                boxes[(r // 3) * 3 + c // 3].add(value)
        
        return True
