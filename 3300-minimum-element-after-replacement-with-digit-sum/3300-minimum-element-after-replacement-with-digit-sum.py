class Solution:
    def minElement(self, nums: List[int]) -> int:
        digit_sum = [sum(map(int , str(x))) for x in nums]
        return min(digit_sum)