class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for x in range(1,len(points)):
            ans += max(abs(points[x][0]-points[x-1][0]),abs(points[x][1]-points[x-1][1]))
        return ans