class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for x in s:
            if stack:
                top = stack[-1]
                if (top=='A' and x =='B') or (top =='C' and x =='D'):
                    stack.pop()
                    continue
            
            stack.append(x)
        
        return len(stack)