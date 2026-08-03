class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ''
        for x in range(0, len(s), k):
            total = 0
            for x in s[x:x+k]:
                total += ord(x) - 97
            
            total = total % 26

            char = chr(total + 97)
            result += char

        return result 
