from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])

        for word in words[1:]:
            freq &= Counter(word)
        res = []
        for char, freq in freq.items():
            res += [char] * freq
        
        return res

