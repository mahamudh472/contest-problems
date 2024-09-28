from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.queue = deque()

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.queue.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.queue.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        return self.queue[0] if self.queue else -1

    def getRear(self) -> int:
        return self.queue[-1] if self.queue else -1
        

    def isEmpty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.max == len(self.queue):
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()