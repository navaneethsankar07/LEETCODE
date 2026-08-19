class Solution:
    def passwordStrength(self, password: str) -> int:
        visited = set()
        strength = 0
        for x in password:
            if x.islower() and x not in visited:
                strength += 1
            elif x.isupper() and x not in visited:
                strength += 2
            elif x.isdigit() and x not in visited:
                strength += 3
            elif x not in visited:
                strength += 5
            
            visited.add(x)
        
        return strength
            