class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        res = [''] * len(s)
        for x in range(len(indices)):
            res[indices[x]] = s[x]
        
        return ''.join(res)
