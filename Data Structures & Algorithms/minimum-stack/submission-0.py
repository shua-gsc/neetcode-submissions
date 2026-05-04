class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            self.mins.append(min(x, self.mins[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


