from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = Counter(nums)

        for x in nums:
            if x % 2 == 0 and freq[x] == 1:
                return x
        
        return -1