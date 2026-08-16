class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        s = list(s)
        if y < x :
            s.sort()
        else:
            s.sort(reverse=True)
        
        return ''.join(s)