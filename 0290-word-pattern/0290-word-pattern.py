class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        freq1 = {}
        freq2 = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for x in range(len(pattern)):
            if pattern[x] in freq1:
                if freq1[pattern[x]] != words[x]:
                    return False
            
            freq1[pattern[x]] = words[x]

            if words[x] in freq2:
                if freq2[words[x]] != pattern[x]:
                    return False
            
            freq2[words[x]] = pattern[x]

        return True