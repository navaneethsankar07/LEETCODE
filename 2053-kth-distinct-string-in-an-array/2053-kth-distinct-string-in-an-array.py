from collections import Counter 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        ans = [x for x,y in freq.items() if y == 1]
        if len(ans) < k:
            return ''
        return ans[k-1]