class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0
        alpha="qwertyuiopasdfghjklzxcvbnm"
        ALPHA="QWERTYUIOPASDFGHJKLZXCVBNM"
        num="1234567890"
        for x in set(password):
            if x in alpha:
                strength+=1
            elif x in ALPHA:
                strength+=2
            elif x in num:
                strength+=3
            else:
                strength+=5
                    
        return strength
            