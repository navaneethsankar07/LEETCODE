class Solution:
    def countEven(self, num: int) -> int:
        def sum_digits(n):
            s = 0
            n = abs(n) 
            while n:
                s += n % 10  
                n //= 10     
            return s
        count = 0
        for x in range(1,num+1):
            if x < 10 and x%2 == 0:
                count += 1
            elif x > 10 and  sum_digits(x)%2==0:
                count += 1
        return count 
