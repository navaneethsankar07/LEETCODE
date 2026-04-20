import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        pqs = []
        for row in grid:
            pq = [v*-1 for v in row]
            heapq.heapify(pq)
            pqs.append(pq)
        
        res = 0

        while any(pqs):
            vals = []
            for pq in pqs:
                vals.append(heapq.heappop(pq) * -1)
        
            res += max(vals)

        return res