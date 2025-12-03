class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        count = 0
        for x in word:
            if x.isupper():
                if x.lower() in word:
                    count += 1
        return count