from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)//2
        for x in nums:
            if freq[x] > n:
                return x
                  