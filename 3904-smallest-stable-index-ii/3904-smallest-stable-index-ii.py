class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        current_min = float('inf')

        for x in range(n-1, -1, -1):
            if nums[x] < current_min:
                current_min = nums[x]
            suffix_min[x] = current_min

        current_max = 0

        for x in range(n):
            if nums[x] > current_max:
                current_max = nums[x]

            if current_max - suffix_min[x] <= k:
                return x
        
        return -1