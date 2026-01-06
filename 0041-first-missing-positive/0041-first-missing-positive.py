class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        x = 1
        while x < len(nums)+2:
            if x not in nums:
                return x
            x+=1 