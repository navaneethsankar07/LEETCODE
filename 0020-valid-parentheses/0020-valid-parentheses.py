class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for x in s:
            if x in pairs:
                if not stack or stack[-1] != pairs[x]:
                    return False
                stack.pop()
            else:
                stack.append(x)

        return len(stack) == 0