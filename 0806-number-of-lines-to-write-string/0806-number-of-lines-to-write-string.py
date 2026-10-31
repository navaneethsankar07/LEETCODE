class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        max_width = 100
        n  = len(s)
        i = 0
        pixels = 0

        while i < n:
            width = widths[ord(s[i]) - 97]
            if max_width - width < 0:
                lines += 1
                max_width = 100 - width
                pixels = width
                i += 1
            else:
                max_width -= width
                i += 1
    
        return [lines, 100 - max_width]


            