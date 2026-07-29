class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            new_digits = ''
            for x in range(len(s)-1):
                new_digits += str((int(s[x]) + int(s[x+1]))%10)
                        
            s = new_digits
        
        return len(set(s)) == 1