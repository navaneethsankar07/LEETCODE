class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        for x in range(len(s)-1):
            if s[x:x+2] in rev:
                return True
            
        return False