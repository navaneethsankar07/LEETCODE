from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
        
            
        if length < len(s):
            length += 1
            

        return length