class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum  = sum(x for x in nums if x <10)
        double_digit_sum  = sum(x for x in nums if x >= 10)
        return single_digit_sum != double_digit_sum