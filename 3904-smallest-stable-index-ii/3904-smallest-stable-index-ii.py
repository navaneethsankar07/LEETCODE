class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for x in range(n-2, -1, -1):
            suffix_min[x] = min(nums[x], suffix_min[x+1])

        prefix_max = 0

        for x in range(n):
            prefix_max = max(nums[x], prefix_max)
            if prefix_max - suffix_min[x] <= k:
                return x
        
        return -1