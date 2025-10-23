class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index = word.index(ch)+1
        rev = word[0:index]
        return rev[::-1] + word[index:]