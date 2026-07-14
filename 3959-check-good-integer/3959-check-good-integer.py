class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        n = str(n)
        digit_sum = 0
        square_sum = 0

        for x in n:
            d = int(x)
            digit_sum += d
            square_sum += d**2
        
        return square_sum - digit_sum >= 50