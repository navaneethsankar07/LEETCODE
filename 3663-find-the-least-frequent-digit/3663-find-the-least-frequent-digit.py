from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = Counter(str(n))
        min_freq = min(freq.values())
        return int(min(x for x,y in freq.items() if y == min_freq))