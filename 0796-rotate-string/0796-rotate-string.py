class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if set(s) != set(goal):
            return False
        
        for x in range(len(s)):
            rotated = s[x:] + s[:x]
            if rotated == goal:
                 return True
        
        return False