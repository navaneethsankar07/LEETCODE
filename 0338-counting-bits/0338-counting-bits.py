class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        while len(ans) <= n:
            ans += [bits + 1 for bits in ans]
        
        return ans[:n+1]