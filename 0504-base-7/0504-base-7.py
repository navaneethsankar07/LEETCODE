class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        res = ""
        n = abs(num)

        while n > 0:
            res += str(n%7)
            n//=7

        res = res[::-1]

        return f"-{res}" if num < 0 else res
            