class MinStack:

    def __init__(self):
        self.s=[]
        self.ms=[]

    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.ms or value <=self.ms[-1]:
            self.ms.append(value)
        

    def pop(self) -> None:
        k=self.s.pop()
        if k==self.ms[-1]:
            self.ms.pop()



    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()