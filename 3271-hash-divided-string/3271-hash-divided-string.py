class Solution:
    def stringHash(self, s: str, k: int) -> str:
        substrings = [s[x:x+k] for x in range(0,len(s),k)]
        result = ''
        for sub in substrings:
            total = 0
            for x in sub:
                total += ord(x) - 97
            
            total = total % 26

            char = chr(total + 97)
            result += char

        return result 
