class Solution:
    def uniformArray(self, A: list[int]) -> bool:
        return min(A) % 2 == 1 or all(a % 2 == 0 for a in A)