from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sfreq = sorted(freq.items(), key = lambda item:item[1] , reverse = True)
        return ''.join([x * y for x,y in sfreq])
