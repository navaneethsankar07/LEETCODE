class Solution:
    def largestOddNumber(self, num: str) -> str:
        for x in range(len(num)-1, -1, -1):
            if num[x] in {'1','3','5','7','9'}:
                return num[:x+1]

        return ''