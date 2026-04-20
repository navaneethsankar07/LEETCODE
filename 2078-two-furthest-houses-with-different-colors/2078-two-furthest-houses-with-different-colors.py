class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        n = len(colors)
        for x in range(n):
            for y in range(n-1,x,-1):
                if colors[x] != colors[y]:
                    max_distance = max(max_distance,y-x)

        return max_distance
