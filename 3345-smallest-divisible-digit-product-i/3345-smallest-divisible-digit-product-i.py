import math
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in range(n,n+10):
            if math.prod(int(digit) for digit in str(x)) % t == 0:
                return x
        