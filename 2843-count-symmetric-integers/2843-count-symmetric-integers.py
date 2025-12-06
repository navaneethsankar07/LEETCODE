class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low,high+1):
            x = list(map(int,str(x)))
            if len(x) % 2 != 0:
                continue
            mid = len(x)//2
            if sum(x[:mid]) == sum(x[mid:]):
                count += 1
        return count
