from itertools import zip_longest

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}

        first_num, sec_num, target_num = "", "", ""

        for x, y, z in zip_longest(firstWord, secondWord, targetWord, fillvalue=' '):
            if x in letters:
                first_num += str(letters[x])
            if y in letters:
                sec_num += str(letters[y])
            if z in letters:
                target_num += str(letters[z])
        
        return int(first_num) + int(sec_num) == int(target_num)