import  re
from  collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        parts =  [word.lower() for word in re.split(r"[!?',;.\s]+", paragraph) if word]
        freq = Counter(parts)
        banned = set(banned)
        
        for word, freq in freq.most_common():
            if word not in banned:
                return word