class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted([int(x) for x in str(num)])

        first = nums[0] * 10 + nums[2]
        second = nums[1] * 10 + nums[3]

        return first + second