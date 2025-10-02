from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        sorted_freq = dict(sorted(freq.items(), key=lambda item:(item[1], -item[0])))
        return [x for x,values in sorted_freq.items() for _ in range(values)]
