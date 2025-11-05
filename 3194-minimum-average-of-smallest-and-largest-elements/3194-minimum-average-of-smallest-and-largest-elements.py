class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        length = len(nums)
        averages = []
        for x in range(length//2):
            averages.append((nums[0]+nums[-1])/2)
            nums = nums[1:-1]
        return min(averages)