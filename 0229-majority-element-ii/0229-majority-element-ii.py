from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)//3
        freq = Counter(nums)
        return [x for x,y in freq.items() if y>length]