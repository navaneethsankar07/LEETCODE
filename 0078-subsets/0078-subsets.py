from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for r in range(len(nums)+1):
            result.extend(combinations(nums,r))
        return result