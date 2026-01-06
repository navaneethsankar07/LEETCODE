class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for x in range(0,1000000):
            if x >0 and  x not in nums:
                return x