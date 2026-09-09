class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        commas = 0
        format = 1000

        while format <= n:
            commas += n - format + 1
            format *= 1000
        
        return commas