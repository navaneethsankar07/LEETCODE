class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        minlen = len(str(low))
        maxlen = len(str(high))
        res = []

        for length in range(minlen, maxlen + 1):
            for x in range(10-length):
                num = int(digits[x:x+length])
                if low <= num <= high:
                    res.append(num)
        
        return res

