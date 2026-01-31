class Solution:
    def greatestLetter(self, s: str) -> str:
        s = ''.join(sorted(s))
        great = ''
        for x in s:
            if x.isupper():
                if x.lower() in s:
                    great = x

        return great