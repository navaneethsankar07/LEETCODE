class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = [x for sublist in grid for x in sublist if x < 0]
        return len(neg)