class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        win_len = 0
        freq = {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            win_len += 1
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                win_len -= 1
                left += 1
            
        return win_len