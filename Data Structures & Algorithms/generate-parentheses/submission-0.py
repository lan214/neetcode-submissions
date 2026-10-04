class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(to_open: int, to_close: int, generated: list[str]):
            if to_open == 0 and to_close == 0:
                res.append("".join(generated))
                return
            
            
            if to_open > 0:
                generated.append("(")
                backtrack(to_open - 1, to_close, generated)
                generated.pop()

            if to_close > 0 and to_open < to_close:
                generated.append(")")
                backtrack(to_open, to_close - 1, generated)
                generated.pop()
            
        backtrack(n, n, [])
        return res