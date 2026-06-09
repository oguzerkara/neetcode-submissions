class MinStack:

    def __init__(self):
        self.stack = []
        self.min_cnt = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_cnt:
            self.min_cnt.append(val)
        else: self.min_cnt.append(min(self.min_cnt[-1],val))
    def pop(self) -> None:
        self.stack.pop()
        self.min_cnt.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_cnt[-1]
