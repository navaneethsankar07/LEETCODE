class Solution:
    def generateTag(self, caption: str) -> str:
        if (caption.strip() == ''):
            return '#'

        res = ""
        arr = caption.split()

        first_word = arr[0].lower()
        res = '#' + first_word

        for x in range(1, len(arr)):
            res += arr[x][0].upper() + arr[x][1:].lower()
        
        return res[:100]
