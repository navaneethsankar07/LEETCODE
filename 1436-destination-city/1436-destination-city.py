class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {x[0] for x in paths}
        for _, dest in  paths:
            if dest not in starts:
                return dest