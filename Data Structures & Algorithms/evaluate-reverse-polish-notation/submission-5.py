class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x,y : y + x,
            '-': lambda x,y : y - x,
            '*': lambda x,y : y * x,
            '/': lambda x,y : int(y/x)
        }
        for token in tokens:
            match token:
                case op if op in operators:
                    if len(stack) < 2:
                        raise RuntimeError("Invalid RPN")
                    stack.append(operators[op](stack.pop(), stack.pop()))
                    print(stack)
                case num:
                    print(int(num))
                    stack.append(int(num))
        return stack.pop()