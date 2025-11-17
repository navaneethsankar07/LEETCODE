class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        words = []
        length = len(s)
        n = 0
        while n < length:
            if length - n >= k:
                words.append(s[n:n+k])
                n+=k
            else:
                words.append(s[n:] +''.join(fill * (k-(length-n))))
                n = length
        return words
