class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        digits = ''.join(map(str,nums))
        for x in digits:
            digit_sum += int(x)
        
        return abs(element_sum - digit_sum)