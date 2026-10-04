class MinStack:

    def __init__(self):
        self.size = 0
        self.stack = list()
        self.mins_idx = list()
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins_idx or val < self.stack[self.mins_idx[-1]]:
            self.mins_idx.append(self.size)
        self.size += 1
        

    def pop(self) -> None:
        self.stack.pop()
        self.size -= 1
        if self.mins_idx[-1] == self.size:
            self.mins_idx.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.mins_idx[-1]]
        
