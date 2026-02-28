class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            temp = start+2*i
            res ^= temp
        
        return res

        