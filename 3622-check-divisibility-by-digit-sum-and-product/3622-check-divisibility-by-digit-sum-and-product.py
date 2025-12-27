class Solution:
    def checkDivisibility(self, n: int) -> bool:
        pro = 1
        total = 0
        num = n
        while n > 0:
            digit = n % 10
            pro *= digit
            total += digit
            n //= 10

        return num % (total+ pro) == 0