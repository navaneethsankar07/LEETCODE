from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        if 1 not in freq.values():
            return -1
        for x,y in freq.items():
            if y == 1:
                return s.index(x)
