class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word[1:].islower() or word.islower():
            return True
        return False