from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        freq = Counter(n)
        score = 0
        n = list(set(n))
        for x in n:
            score += int(x)*freq[x]

        return score        


