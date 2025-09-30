class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        for x in range(length):
            if len(nums) != 1:
                newNums = []
                for x in range(len(nums)-1):
                    newNums.append((nums[x] + nums[x+1]) % 10)
                nums = newNums
        return nums[0]