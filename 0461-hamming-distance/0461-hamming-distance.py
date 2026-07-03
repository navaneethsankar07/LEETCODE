class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference = x^y
        return bin(difference).count('1')

