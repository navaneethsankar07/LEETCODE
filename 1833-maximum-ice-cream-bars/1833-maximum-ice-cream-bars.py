class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_creams = 0
        for x in costs:
            if coins >= x:
                ice_creams += 1
                coins -= x
            else:
                break

        return ice_creams
