class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = []
        
        for x in range(rowIndex + 1):
            row = [0] * (x + 1)
            row[0] = row[-1] = 1
            for j in range(1 , x):
                row[j] = dp[x - 1][j - 1] + dp[x - 1][j]
            
            dp.append(row)
        
        return dp[rowIndex]