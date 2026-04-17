class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        res = float('inf')

        for i, x in enumerate(nums):
            if x in seen:
                res = min(res, i - seen[x])
            
            seen[int(str(x)[::-1])] = i
        
        return -1 if res == float('inf') else res
