class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        indexes = {y:x for x , y in enumerate(s)}
        res = 0
        for x in range(len(t)):
            res += abs(indexes[t[x]] - x)
        
        return res
