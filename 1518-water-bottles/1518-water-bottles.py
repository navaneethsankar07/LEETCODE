class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked = numBottles
        while numBottles >= numExchange:
            rem = numBottles % numExchange
            new = numBottles // numExchange
            drinked += new
            numBottles = new + rem
        return drinked 
    