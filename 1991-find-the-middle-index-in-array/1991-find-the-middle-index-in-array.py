class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum (nums)
        for x in range(len(nums)):
            if left == right-nums[x]:
                return x
            left += nums[x]
            right -= nums[x]
        
        return -1