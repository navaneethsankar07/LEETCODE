class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        
        for x in range(len(s)-1):
            if abs(int(s[x]) - int(s[x+1])) > 2:
                return False
        
        return True