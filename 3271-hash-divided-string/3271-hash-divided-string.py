class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
                
        for x in range(0,len(s), k):
            hashedChar = 0
            for l in s[x:x+k]:
                hashedChar += ord(l) - 97
            
            result +=  chr((hashedChar % 26) + 97)
        
        return result