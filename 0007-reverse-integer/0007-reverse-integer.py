class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        reversed = int(str(abs(x))[::-1])
        
        return reversed * sign if reversed < 2**31 -1 and reversed > -2**31 else 0