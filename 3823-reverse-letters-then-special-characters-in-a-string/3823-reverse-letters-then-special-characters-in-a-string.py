class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            elif s[left].isalpha() and s[right].isalpha() == False:
                right -= 1
            
            elif s[right].isalpha() and s[left].isalpha() == False:
                left += 1
            else:
                left += 1
                right -= 1
            
        
        left = 0 
        right = len(s) -1

        while left <= right:
            if s[left].isalpha():
                left += 1
            
            elif s[right].isalpha():
                right -= 1
            
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return "".join(s)