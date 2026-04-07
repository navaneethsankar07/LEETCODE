class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ':' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for x in key:
            if x not in mapping:
                mapping[x] = letters[i]
                i += 1

        for char in message:
            res += mapping[char]
        
        return res