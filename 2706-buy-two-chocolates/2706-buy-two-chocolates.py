class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        if len(prices) < 2 or prices[0] + prices[1] > money:
            return money
        else:
            return money - (prices[0] + prices[1])
