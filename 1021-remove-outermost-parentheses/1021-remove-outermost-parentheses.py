class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = []
        start = 0

        for i,x in enumerate(s):
            if x == '(':
                count +=1
            else:
                count -=1

            if count == 0:
                result.append(s[start+1:i])
                start = i+1
        return ''.join(result)