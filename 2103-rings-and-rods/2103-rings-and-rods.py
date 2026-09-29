class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for x in range(len(rings) - 1, -1, -2):
            rod = rings[x]
            color = rings[x - 1]

            rods.setdefault(rod, set()).add(color)
        count = 0
        for x in rods.values():
            if len(x) == 3:
                count += 1
        
        return count

