class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        star = 0 
        for x in range(len(s)):
            if s[x] == '|':
                count += 1
            if count & 1 == 0 and s[x] == '*':
                star += 1
        return star

