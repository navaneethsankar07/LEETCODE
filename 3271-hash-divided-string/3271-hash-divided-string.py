class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        substrings = [s[x:x+k] for x in range(0,len(s), k)]
        
        for x in substrings:
            hashedChar = 0
            for l in x:
                hashedChar += ord(l) - 97
            
            result +=  chr((hashedChar % 26) + 97)
        
        return result