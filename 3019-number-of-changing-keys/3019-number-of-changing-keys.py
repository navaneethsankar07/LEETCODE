class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        length = len(s)
        for x in range(1,length):
            if s[x].lower() != s[x-1].lower():
                count += 1
        return count