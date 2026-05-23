class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0

        for x in nums:
            if x % 6 == 0:
                total += x
                count += 1
        
        return total//count if count != 0 else 0