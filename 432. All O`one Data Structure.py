class AllOne:

    def __init__(self):
        self.d = {}

    def inc(self, key: str) -> None:
        if key in self.d:
            self.d[key] += 1
        else:
            self.d[key] = 1

    def dec(self, key: str) -> None:
        if key in self.d:
            if self.d[key] > 1:
                self.d[key] -= 1
            else:
                self.d.pop(key)


    def getMaxKey(self) -> str:
        max_val = max(self.d.values(), default=0)
        if max_val == 0:
            return ""
        for i, j in self.d.items():
            if j==max_val:
                return i

    def getMinKey(self) -> str:
        min_val = min(self.d.values(), default=0)
        if min_val == 0:
            return ""
        for i, j in self.d.items():
            if j==min_val:
                return i


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
# obj.inc("hello")
# obj.inc("goodbye")
obj.inc("hello")
obj.inc("hello")
# obj.dec()
param_3 = obj.getMaxKey()
param_3 = obj.getMinKey()
obj.inc("leet")
param_3 = obj.getMaxKey()
param_3 = obj.getMinKey()
# obj.inc("code")
# obj.inc("leet")
# obj.dec("hello")
# obj.inc("leet")
# obj.inc("code")
# obj.inc("code")
# param_4 = obj.getMinKey()
# obj.inc("leet")
# param_5 = obj.getMaxKey()
# param_6 = obj.getMinKey()