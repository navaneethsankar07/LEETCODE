class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        commas = 0
        factor = 1000
        while factor <= n:
            commas += (n - factor + 1)
            factor *= 1000
            
        return commas
