from collections import deque
class RecentCounter:

    def __init__(self):
        self.recent_request = deque([])


    def ping(self, t: int) -> int:
        self.recent_request.append(t)
        while self.recent_request[0] < t-3000:
            self.recent_request.popleft()
        
        return len(self.recent_request)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)