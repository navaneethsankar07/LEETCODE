class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for x in range(len(words)):
            for j in range(x):
                if set(words[x]) == set(words[j]):
                    count += 1

        return count