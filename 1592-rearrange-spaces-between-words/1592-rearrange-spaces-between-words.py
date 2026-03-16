class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        n = len(words)
        if n == 1:
            return words[0] + ' ' * spaces

        space_between = spaces // (n -1)
        extra = spaces % (n - 1)
    
        return  (' ' * space_between).join(words) + (' ' * extra)