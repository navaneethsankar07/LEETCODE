class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        champ = 0 
        one_count = 0
        for x in grid:
            if 1 in x and x.count(1)>one_count:
                champ = grid.index(x)
                one_count = x.count(1)
        return champ