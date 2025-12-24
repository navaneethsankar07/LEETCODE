class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        current = 0
        max_vowel = 0
        left, right = 0, k
        for x in range(left,right):
                if s[x] in vowel:
                    current += 1
        while right < len(s):
            
            max_vowel = max(max_vowel,current)
            if s[left] in vowel:
                current -= 1
            left += 1
            if s[right] in vowel:
                current += 1
            right += 1
        max_vowel = max(max_vowel,current)
        return max_vowel
        