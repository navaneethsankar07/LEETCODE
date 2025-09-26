import string
class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = list(string.ascii_lowercase)
        alphabet.sort(reverse=True)
        degree = 0
        for index , x in enumerate(s):
            num = alphabet.index(x)+1
            num *= index +1
            degree += num
            
        return degree