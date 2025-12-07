class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for x in range(1,len(nums)):
            if nums[x] % 2 == (nums[x-1]) % 2:
                return False
        return True