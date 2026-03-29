class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for let in s:
            if stack and abs(ord(let) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(let)
        
        return  ''.join(stack)
                
