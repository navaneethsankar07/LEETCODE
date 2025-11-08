
from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = Counter(arr)
        for x, y in freq.items():
            if y == max(freq.values()):
                return x