class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        x = str(x)
        if x not in n or n[0] == x:
            return False
        
        return True