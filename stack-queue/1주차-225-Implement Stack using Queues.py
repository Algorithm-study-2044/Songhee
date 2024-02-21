from collections import deque

class MyStack:

    def __init__(self):
        self.ms = deque()

    def push(self, x: int) -> None:
        self.ms.append(x)

    def pop(self) -> int:
        return self.ms.pop()

    def top(self) -> int:
        tmp = self.ms.pop()
        self.ms.append(tmp)
        return tmp

    def empty(self) -> bool:
        return len(self.ms) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()