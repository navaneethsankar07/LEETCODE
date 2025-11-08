
from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        a = len(arr)//4
        freq = Counter(arr)
        for x, y in freq.items():
            if y > a:
                return x