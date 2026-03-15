from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        freq = Counter(chars)
        for word in words:
            word_count = Counter(word)
        
            if all(word_count[c] <= freq[c] for c in word_count):
                res += len(word)

        return res