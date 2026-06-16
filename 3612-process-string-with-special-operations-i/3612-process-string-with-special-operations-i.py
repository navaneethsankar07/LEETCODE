class Solution:
    def processStr(self, s: str) -> str:
        res = ''
        for x in s:
            if x.isalpha():
                res += x
            elif x == '*':
                res = res[:-1]
            elif x == '#':
                res += res
            elif x == '%':
                res = res[::-1]
        
        return res