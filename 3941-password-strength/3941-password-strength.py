class Solution:
    def passwordStrength(self, password: str) -> int:
        a=list(set(password))
        alpha="qwertyuiopasdfghjklzxcvbnm"
        ALPHA="QWERTYUIOPASDFGHJKLZXCVBNM"
        num="1234567890"
        result=0
        for x in a:
            if x in alpha:
                result+=1
            elif x in ALPHA:
                result+=2
            elif x in num:
                result+=3
            else:
                result+=5
        return result
        