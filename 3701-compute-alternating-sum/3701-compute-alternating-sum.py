class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sum = 0
        length = len(nums)
        for x in range(length):
            if x & 1 == 0:
                sum += nums[x]
            else:
                sum -= nums[x]
        return sum