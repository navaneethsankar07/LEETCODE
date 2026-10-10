class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        ans = 0
        for x in range(len(sorted_points) - 1):
            diff = sorted_points[x + 1][0] - sorted_points[x][0]
            if diff > ans:
                ans = diff
        
        return ans