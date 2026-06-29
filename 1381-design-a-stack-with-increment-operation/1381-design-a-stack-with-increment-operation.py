class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.top = -1

    def push(self, x: int) -> None:
        print(self.stack)
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.top += 1

    def pop(self) -> int:
        print(self.stack)
        if self.top > -1:
            self.top -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        print(self.stack)
        if len(self.stack) < k:
            self.stack = [x+val for x in self.stack]
        else:
            for x in range(k):
                self.stack[x] += val
                


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)