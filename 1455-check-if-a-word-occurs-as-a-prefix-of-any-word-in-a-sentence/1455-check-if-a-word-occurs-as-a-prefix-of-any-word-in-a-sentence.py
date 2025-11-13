class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for x in words:
            if x.startswith(searchWord):
                return words.index(x) + 1
        return -1