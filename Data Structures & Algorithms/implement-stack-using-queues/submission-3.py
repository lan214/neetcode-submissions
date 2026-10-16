class MyStack:

    def __init__(self):
        self.queue = deque()
        self.my_top = None

    def push(self, x: int) -> None:
        if self.my_top:
            self.queue.append(self.my_top)
        self.my_top = x

    def pop(self) -> int:
        # if self.emtpy():
        #     raise Exception("Stack empty")
        top = self.my_top
        queue_size = len(self.queue)
        for _ in range(queue_size - 1):
            self.queue.append(self.queue.popleft())
        if self.queue:
            self.my_top = self.queue.popleft()
        else:
            self.my_top = None
        return top
        

    def top(self) -> int:
        if self.empty():
            raise Exception("Stack empty")
        return self.my_top

    def empty(self) -> bool:
        return self.my_top is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()