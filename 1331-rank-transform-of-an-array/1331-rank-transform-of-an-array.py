class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {values: index+1 for index, values in enumerate(sorted(set(arr)))}
        return [ranks[x] for x in arr]