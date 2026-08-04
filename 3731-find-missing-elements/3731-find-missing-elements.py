class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        min_ = min(nums)
        max_ = max(nums)
        for x in range(min_, max_):
            if x not in nums:
                res.append(x)
        
        return res