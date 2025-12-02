class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        num = str(bin(n))
        if num == num[::-1]:
            return True
        return False
