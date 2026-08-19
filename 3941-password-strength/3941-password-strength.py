class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0
        for x in set(password):
            if x in '!@#$':
                strength += 5
            elif x.islower() :
                strength += 1
            elif x.isupper():
                strength += 2
            elif x.isdigit():
                strength += 3
                    
        return strength
            