class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        return[x for x in range(len(nums)) if nums[x] == target]