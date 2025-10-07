class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        divisor = 1
        for x in range(1,nums[0]+1):
            if nums[0]%x == 0 and nums[-1] %x == 0 and x>divisor:
                divisor = x
        return divisor