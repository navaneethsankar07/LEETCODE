class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        for x in range(len(colors)):
            for y in range(len(colors)-1,x,-1):
                if colors[x] != colors[y]:
                    max_distance = max(max_distance,y-x)

        return max_distance
