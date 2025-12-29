class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s)-1
        ans = list(s)
        while left < right:
            if not ans[left].isalpha():
                left += 1
            elif not ans[right].isalpha():
                right -= 1
            else:
                ans[left], ans[right] = ans[right],ans[left]
                left += 1
                right -= 1
                

        return ''.join(ans)