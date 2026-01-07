class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_pointer = 0
        res = []
        for char in range(len(s)):
            while s_pointer < len(spaces) and char == spaces[s_pointer]:
                res.append(' ')
                s_pointer += 1
            res.append(s[char])
        return ''.join(res)