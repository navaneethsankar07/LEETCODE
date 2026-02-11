class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for x in prices[1:]:
            max_profit = max(max_profit,x-min_price)
            min_price = min(min_price,x)
        
        return max_profit
