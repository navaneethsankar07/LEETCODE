class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        if n <= 8:
            return n

        total = 8
        remaining = n - 8
        presses = 2

        while remaining > 0:
            letter = min(8, remaining)
            total += letter * presses
            remaining -= letter
            presses += 1
        
        return total