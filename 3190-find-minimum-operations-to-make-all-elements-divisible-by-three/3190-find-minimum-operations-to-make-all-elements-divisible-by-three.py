class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0 
        for x in nums:
            if x % 3 != 0:
                lower = x - (X%3)
                upper = lower + 3
                count += min(abs(x - lower) , abs(x - upper))
        return count