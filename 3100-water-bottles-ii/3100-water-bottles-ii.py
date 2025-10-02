class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drinked = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            drinked +=1
            numBottles += 1
            numExchange += 1
        return drinked