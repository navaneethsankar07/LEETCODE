class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        length = len(s)
        count1 = 0
        count2 = 0
        for x in range(length):
            if x < length//2 and s[x] in vowels:
                count1 +=1
            elif x>= length//2 and s[x] in vowels: 
                count2 +=1
        if count1 == count2:
            return True
        return False