class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        for x in costs:
            if coins >= x:
                total += 1
                coins -= x
        return total