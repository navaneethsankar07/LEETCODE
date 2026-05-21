from collections import Counter
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        freq = Counter(bulbs)
        result = [x for x,y in freq.items() if y%2==1]
        result.sort()
        return result