class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(1,n+1):
            if '0' not in  str(n-x) and '0' not in  str(x):
                return [x,n-x] 
