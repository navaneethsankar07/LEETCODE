class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            if len(str(x)) > 1:
                max_digit = max(str(x))
                new_num = max_digit * len(str(x))
                total += int(new_num)
            
            else:
                total += x
        
        return total
