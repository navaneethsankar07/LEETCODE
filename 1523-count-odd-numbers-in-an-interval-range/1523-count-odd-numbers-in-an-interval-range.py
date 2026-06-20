class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_high = (high + 1) // 2
        odd_low = (low ) // 2
        return odd_high - odd_low 