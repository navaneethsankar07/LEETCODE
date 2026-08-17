class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            max_digit = 0
            ones_base = 0

            while x > 0:
                digit = x % 10
                if digit > max_digit:
                    max_digit = digit

                ones_base = ones_base * 10 + 1

                x //= 10
            
            total +=  max_digit * ones_base
        
        return total
