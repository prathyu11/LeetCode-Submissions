class MinStack:

    def __init__(self):
        self.st = []
        self.ms = []

    def push(self, val: int) -> None:
        self.st.append(val)
        current_min = self.ms[-1] if self.ms else val
        self.ms.append(min(current_min,val))

    def pop(self) -> None:
        self.st.pop()
        self.ms.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
