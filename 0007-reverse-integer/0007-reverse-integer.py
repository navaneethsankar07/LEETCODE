class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            digit = x % 10
            reversed = (reversed * 10) + digit
            x //= 10
        return reversed * sign if reversed < 2**31 -1 and reversed > -2**31 else 0