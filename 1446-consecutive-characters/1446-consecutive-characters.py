class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1

        for x in range(1,len(s)):
            if s[x] != s[x-1]:
                max_count = max(max_count, count)
                count = 1
            else:
                count += 1
        max_count = max(max_count, count)
        return max_count