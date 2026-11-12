from collections import Counter
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq = Counter(nums)
        return max(freq, key=freq.get)