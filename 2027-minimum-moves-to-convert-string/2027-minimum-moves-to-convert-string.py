class Solution:
    def minimumMoves(self, s: str) -> int:
        min_moves = x = 0

        while x < len(s):
            if s[x] == 'X':
                min_moves += 1
                x += 3
            
            else:
                x += 1
            
        return min_moves