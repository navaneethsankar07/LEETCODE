class Solution:
    def balancedStringSplit(self, s: str) -> int:
        maximum_count = 0
        val = 0
        for x in s:
            val += 1 if x == 'R' else -1
            if val == 0:
                maximum_count += 1
        return maximum_count