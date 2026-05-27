class Solution:
    def maxPower(self, s: str) -> int:
        max_ = 1
        count = 1
        curr = s[0]
        for x in s[1:]:
            if x == curr:
                count += 1
            
            else:
                curr = x
                count = 1
            
            max_ = max(max_, count)
        
        return max_