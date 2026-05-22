class Solution:
    def maxProduct(self, n: int) -> int:
        str_n = list(str(n))
        str_n.sort()
        return int(str_n[-1]) * int(str_n[-2])