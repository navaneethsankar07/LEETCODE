class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        start = 0
        result = []
        count = 0

        for i, x in enumerate(s):
            if x == "(":
                count += 1
            else:
                count -= 1
            
            if count == 0:
                result.append(s[start+1:i])
                start = i+1
        
        return ''.join(result)