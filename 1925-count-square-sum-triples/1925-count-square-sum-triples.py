import math
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                c_sqr = a * a + b * b
                c = int(c_sqr ** 0.5 )

                if c * c == c_sqr and c <= n:
                    count += 2
        
        return count