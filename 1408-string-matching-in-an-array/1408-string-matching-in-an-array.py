class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        n = len(words)
        for x in range(n):
            for y in range(n):
                if x != y and words[x] in words[y]:
                    res.append(words[x])
                    break
                
        return res
        