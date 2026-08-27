class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total = 0
        last = 0
        for x in requests:
            total += abs(last - x)
            last = x
        
        return total