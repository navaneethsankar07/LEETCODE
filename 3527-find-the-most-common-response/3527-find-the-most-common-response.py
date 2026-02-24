from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = Counter(set(responses[0]))
        for x in range(1,len(responses)):
            for res in set(responses[x]):
                freq[res] = freq.get(res,0) + 1
        return min(freq,key=lambda k: (-freq[k],k))
