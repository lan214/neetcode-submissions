class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (-1, 0), (1, 0)]
        def dfs(row: int, col: int, next_to_find: int) -> bool:
            if next_to_find == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[next_to_find]:
                return False
            
            letter = board[row][col]
            board[row][col] = "."

            for rd, cd in directions:
                if dfs(row + rd, col + cd, next_to_find + 1):
                    return True

            board[row][col] = letter

            return False
            
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False