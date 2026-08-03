class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ''
        total = 0

        for i, char in enumerate(s):
            total += ord(char) - 97

            if (i+1) % k == 0:
                result += chr((total%26) + 97)
                total = 0
        
        return result 