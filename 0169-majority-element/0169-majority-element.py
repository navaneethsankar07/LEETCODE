from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        length = len(nums)//2
        for x,y in freq.items():
            if y>length:
                return x
                