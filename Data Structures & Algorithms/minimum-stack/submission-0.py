class MinStack:

    def __init__(self):
        self.stack = []
        self.extra_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.extra_stack[-1] if self.extra_stack else val)
        self.extra_stack.append(val)

    def pop(self) -> None:
        
        if self.stack:
            self.stack.pop()
            self.extra_stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.extra_stack:
            return self.extra_stack[-1]
