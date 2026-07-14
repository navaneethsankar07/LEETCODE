class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        n = str(n)
        digit_sum = 0
        square_sum = 0

        for x in n:
            digit_sum += int(x)
            square_sum += int(x)**2
        
        return square_sum - digit_sum >= 50