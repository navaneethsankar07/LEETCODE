class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        copy = words[:]
        for x in words:
            print(words)
            if x[::-1] in copy and words.index(x) != words.index(x[::-1]):
                count += 1
                copy.remove(x)
                copy.remove(x[::-1])
        return count
