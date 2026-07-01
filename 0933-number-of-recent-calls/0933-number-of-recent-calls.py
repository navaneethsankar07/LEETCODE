from collections import deque
class RecentCounter:

    def __init__(self):
        self.pings = []
        self.start = 0


    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[self.start] < t-3000:
            self.start += 1
        
        return len(self.pings) - self.start
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)