class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        x = max(1, sum(nums) // len(nums) + 1)

        while x in nums:
            x += 1

        return x