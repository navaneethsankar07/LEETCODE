class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {'a':0,'b':0,'c':0}
        result = 0
        for right in range(len(s)):
            count[s[right]] += 1

            while all(value > 0 for value in count.values()):
                result += len(s)-right
                count[s[left]] -= 1
                left += 1
        
        return result
