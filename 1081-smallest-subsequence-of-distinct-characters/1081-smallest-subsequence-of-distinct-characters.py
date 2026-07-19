from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []

        for x in s:
            freq[x] -= 1
            if x in seen:continue

            while stack and stack[-1] > x and freq[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(x)
            seen.add(x)
        
        return "".join(stack)
