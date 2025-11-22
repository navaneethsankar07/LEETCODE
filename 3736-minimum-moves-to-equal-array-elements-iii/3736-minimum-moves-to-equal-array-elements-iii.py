class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        count = 0
        for x in nums:
            count += (maxi-x)

        return count