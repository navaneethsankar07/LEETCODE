from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        return sum([x*y for x,y in freq.items() if y%k==0])