class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for x in range(n+1):
            binary = bin(x).count('1')
            ans.append(binary)
        
        return ans