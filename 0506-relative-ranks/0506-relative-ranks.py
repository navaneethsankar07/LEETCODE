class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        res = {}
        for i, x  in enumerate(sorted_score):
            if i == 0:
                res[x] = 'Gold Medal'
            elif i == 1:
                res[x] = 'Silver Medal'
            elif i == 2:
                res[x] = 'Bronze Medal'
            else:
                res[x] = str(i+1)

        return [res[s] for s in score]