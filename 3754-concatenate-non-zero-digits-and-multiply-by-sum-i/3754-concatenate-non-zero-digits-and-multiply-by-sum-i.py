class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = [int(x) for x in str(n) if x != '0']
        if not x :
            return 0
        
        num = int(''.join(map(str,x)))
        return num * sum(x)