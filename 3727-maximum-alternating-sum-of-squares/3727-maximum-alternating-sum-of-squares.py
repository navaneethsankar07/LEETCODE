class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x*x for x in nums)

        n = len(nums) // 2

        return sum(a[n:]) - sum(a[:n])