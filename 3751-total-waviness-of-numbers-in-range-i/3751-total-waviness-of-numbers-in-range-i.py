class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for x in range(num1,num2+1):
            x = str(x)
            for digit in range(1,len(x)-1):
                if x[digit] > x[digit-1] and x[digit] > x[digit+1]:
                    res += 1
                elif x[digit] < x[digit-1] and x[digit] < x[digit+1]:
                    res += 1
        
        return res
       
