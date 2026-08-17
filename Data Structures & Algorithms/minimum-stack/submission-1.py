class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)
        m = val if len(self.ms)==0 else min(self.ms[-1],val)
        self.ms.append(m)
        

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return self.ms[-1]
