class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        for x in range(len(s)):
            if s[x] != ('0' if x%2 == 0 else '1'):
                count1 += 1
            
            if s[x] != ('0' if x%2 != 0 else '1'):
                count2 += 1
        
        return min(count1,count2)