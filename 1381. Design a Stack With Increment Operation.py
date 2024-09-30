class CustomStack:

    def __init__(self, maxSize: int):
        self.l = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.l)<self.maxSize:
            self.l.append(x)

    def pop(self) -> int:
        if not len(self.l)==0:
            top = self.l[-1]
            self.l.pop()
            return top
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        r = k if len(self.l)>=k else len(self.l)
        for i in range(r):
            self.l[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)