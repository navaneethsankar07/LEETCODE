class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        nums_ = ''.join(map(str,nums))
        return nums_.count(str(digit))