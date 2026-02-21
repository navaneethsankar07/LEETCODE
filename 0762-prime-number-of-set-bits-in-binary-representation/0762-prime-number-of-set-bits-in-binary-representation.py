class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(num):
            if num <=1 :
                return False
            if num <=3:
                return True
            if num % 2 == 0 or num %3 == 0:
                return False
            
            i = 5
            while i*i <= num:
                if num%i == 0:
                    return False
            return True
            
        
        count = 0
        for x in range(left,right+1):
            bit = bin(x)[2:]
            if isPrime(bit.count('1')):
                count += 1
    
        return count