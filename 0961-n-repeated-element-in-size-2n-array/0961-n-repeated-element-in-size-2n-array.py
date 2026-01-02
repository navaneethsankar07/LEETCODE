from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)//2
        for x, y in freq.items():
            if y == n:
                return x