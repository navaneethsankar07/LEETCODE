class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        temp = [False] * (n + 1)
        temp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if temp[j] and s[j:i] in words:
                    temp[i] = True
                    break
        
        return  temp[n]