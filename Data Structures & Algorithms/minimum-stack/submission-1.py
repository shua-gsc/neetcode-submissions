# tuple variation
class MinStack:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []

    def push(self, x) -> None:
        self.stack.append((x, min(x, self.stack[-1][1]) if self.stack else x))
    
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


