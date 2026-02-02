class Solution:
    def alternateDigitSum(self, n: int) -> int:
        neg = False
        digit_sum = 0
        for x in str(n):
            if neg == False:
                digit_sum += int(x)
                neg = True
            else:
                digit_sum -= int(x)
                neg = False

        return digit_sum