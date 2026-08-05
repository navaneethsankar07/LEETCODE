class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        if s[-1] not in vowels:
            return s
        
        s = list(s)

        while s and s[-1] in vowels:
            s.pop()
        
        return ''.join(s)