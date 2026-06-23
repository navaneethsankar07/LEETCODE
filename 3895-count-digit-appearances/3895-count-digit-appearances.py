class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        nums = str(nums)
        return nums.count(str(digit))