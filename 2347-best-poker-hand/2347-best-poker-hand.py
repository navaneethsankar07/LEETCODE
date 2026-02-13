from collections import Counter
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        freq = Counter(ranks)
        if max(freq.values()) >= 3:
            return 'Three of a Kind'
        elif 2 in freq.values():
            return 'Pair'
        else:
            return 'High Card'