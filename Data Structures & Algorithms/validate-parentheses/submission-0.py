from collections import deque

class Solution:
    def __init__(self):
        self.matches = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != self.matches[c]:
                    return False
        return not stack