class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        
        words = [""] * numRows
        temp = 0
        step = 1

        for x in s:
            words[temp] += x

            if temp  == 0:
                step = 1
            elif temp == numRows - 1 :
                step = -1
            
            temp += step
        
        return "".join(words)
