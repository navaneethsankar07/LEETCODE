class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        n = len(prices)
        for x in range(n):
            for y in range(x+1, n):
                if prices[y] <= prices[x]:
                    ans.append(prices[x]-prices[y])
                    break
            else:
                ans.append(prices[x])
        
        return ans