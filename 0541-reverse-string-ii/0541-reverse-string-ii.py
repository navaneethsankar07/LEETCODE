class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for x in range(0,len(s), 2*k):
            res.append(s[x:x+k][::-1])
            res.append(s[x+k:x+2*k])
        
        return ''.join(res)