class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        res = []
        count = 0
        for x in range(len(s)-1,-1,-1):
            res.append(s[x])
            count+=1

            if count == k:
                res.append('-')
                count = 0
        
        if res and res[-1] == '-':
            res.pop()

        return ''.join(res[::-1])