class Solution:
    def residuePrefixes(self, s: str) -> int:
        count = 0
        seen = set()
        for i, x in enumerate(s):
            seen.add(x)
            if len(seen) == (i+1) % 3:
                count += 1
        
        return count
